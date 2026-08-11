#!/usr/bin/env python3
"""
CodeHouse — módulo de agendamento de reuniões com clientes.

Usa o google_api.py do skill google-workspace (já autenticado) para:
  - achar o próximo horário livre na agenda do Millani
  - criar evento marcado com a tag [CodeHouse] + #codehouse

Convenção de tagging (obrigatória p/ tudo que for CodeHouse):
  - summary:  "[CodeHouse] <tipo> — <cliente>"
  - description: metadados + "#codehouse" no corpo

Reaproveita o CLI do skill via subprocess (contrato estável de JSON).
"""

import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone

# ponytail: usa o google_api.py autenticado em vez de reimplementar OAuth
GAPI = r"C:\Users\Admin\AppData\Local\hermes\skills\productivity\google-workspace\scripts\google_api.py"
TZ = "America/Sao_Paulo"  # fuso do Millani

# Janela de trabalho p/ busca de slot (horário comercial BR)
WORK_START_H = 9
WORK_END_H = 18
DEFAULT_DURATION_MIN = 30
LOOKAHEAD_DAYS = 14


def _run(args):
    cmd = ["python", GAPI] + args
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"google_api falhou: {res.stderr.strip()}")
    out = res.stdout.strip()
    if not out:
        return []
    return json.loads(out)


def list_events(start=None, end=None, max_n=50):
    args = ["calendar", "list"]
    if start:
        args += ["--start", start]
    if end:
        args += ["--end", end]
    args += ["--max", str(max_n)]
    return _run(args)


def _parse_start(ev):
    s = ev.get("start", "")
    # aceita "2026-08-16" (all-day) ou ISO completo
    try:
        if "T" in s:
            return datetime.fromisoformat(s)
        return datetime.fromisoformat(s + "T00:00:00")
    except Exception:
        return None


def find_free_slot(duration_min=DEFAULT_DURATION_MIN,
                   lookahead_days=LOOKAHEAD_DAYS,
                   work_start=WORK_START_H,
                   work_end=WORK_END_H,
                   skip_weekends=True):
    """Retorna (start_iso, end_iso) do primeiro slot livre, ou None."""
    now = datetime.now()
    # arredonda para o próximo quarto de hora
    base = now + timedelta(minutes=(15 - now.minute % 15) % 15)
    end_look = now + timedelta(days=lookahead_days)

    # busca eventos no período
    evs = list_events(
        start=base.strftime("%Y-%m-%dT%H:%M:%SZ"),
        end=end_look.strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
    busy = []
    for e in evs:
        s = _parse_start(e)
        en = e.get("end", "")
        try:
            if "T" in en:
                ee = datetime.fromisoformat(en)
            else:
                ee = datetime.fromisoformat(en + "T23:59:59")
        except Exception:
            ee = None
        if s and ee:
            busy.append((s, ee))
    busy.sort()

    slot = timedelta(minutes=duration_min)
    cursor = base
    for _ in range(lookahead_days * 24 * 4):  # iter limite
        # pula fora da janela de trabalho
        if cursor.hour < work_start or cursor.hour >= work_end:
            # avança para o início do próximo dia útil
            cursor = cursor.replace(hour=work_start, minute=0, second=0, microsecond=0)
            cursor += timedelta(days=1)
            if skip_weekends and cursor.weekday() >= 5:
                cursor += timedelta(days=2 - cursor.weekday())
            continue
        cand_end = cursor + slot
        conflict = any(not (cand_end <= b[0] or cursor >= b[1]) for b in busy)
        if not conflict and cand_end.hour <= work_end:
            # gera ISO com fuso
            s_iso = cursor.strftime("%Y-%m-%dT%H:%M:%S") + "-03:00"
            e_iso = cand_end.strftime("%Y-%m-%dT%H:%M:%S") + "-03:00"
            return s_iso, e_iso
        cursor += timedelta(minutes=15)
        if cursor >= end_look:
            break
    return None


def book(client_name, client_email=None, duration_min=DEFAULT_DURATION_MIN,
         meeting_type="Reunião", dry_run=False, slot=None):
    """Agenda reunião CodeHouse. dry_run=True só mostra o que faria."""
    if slot is None:
        slot = find_free_slot(duration_min=duration_min)
    if not slot:
        return {"status": "no_slot", "message": "Nenhum horário livre no período."}
    s_iso, e_iso = slot

    summary = f"[CodeHouse] {meeting_type} — {client_name}"
    description = (
        f"Reunião agendada via agente CodeHouse.\n"
        f"Cliente: {client_name}\n"
        f"Tipo: {meeting_type}\n"
        f"#codehouse\n"  # tag obrigatória
    )
    attendees = client_email if client_email else ""

    if dry_run:
        return {
            "status": "dry_run",
            "summary": summary,
            "start": s_iso,
            "end": e_iso,
            "attendees": attendees,
        }

    args = ["calendar", "create",
            "--summary", summary,
            "--start", s_iso,
            "--end", e_iso,
            "--description", description]
    if attendees:
        args += ["--attendees", attendees]
    return _run(args)


if __name__ == "__main__":
    # CLI mínimo: python codehouse_book.py book --client "Nome" --email x@y.com
    import argparse
    p = argparse.ArgumentParser(description="CodeHouse scheduling")
    sub = p.add_subparsers(dest="cmd")

    pf = sub.add_parser("find-free", help="Mostra próximo slot livre")
    pf.add_argument("--duration", type=int, default=DEFAULT_DURATION_MIN)

    pb = sub.add_parser("book", help="Agenda reunião CodeHouse")
    pb.add_argument("--client", required=True)
    pb.add_argument("--email", default="")
    pb.add_argument("--type", default="Reunião")
    pb.add_argument("--duration", type=int, default=DEFAULT_DURATION_MIN)
    pb.add_argument("--dry", action="store_true", help="Não cria, só mostra")

    a = p.parse_args()
    if a.cmd == "find-free":
        print(json.dumps(find_free_slot(duration_min=a.duration), indent=2))
    elif a.cmd == "book":
        print(json.dumps(book(a.client, a.email, a.duration, a.type, dry_run=a.dry), indent=2))
    else:
        p.print_help()
