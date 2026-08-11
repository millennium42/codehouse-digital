"""Persona do agente de prospecção + geração de respostas coerentes.

Pablo, representante comercial da Code House. Mantém contexto da conversa
por lead (histórico) e usa os dados do lead (dores, segmento) para falar
com naturalidade. No fim, envia o link de agendamento.

Tom: humano, direto, sem jargão de robô. Usa o humanizer no pós-processamento.
"""
from __future__ import annotations

from src.db import Lead, Message
from src.scorer import Enrichment
from src.llm_client import chat_completion, chat_completion_json
from src.humanizer import humanize

PERSONA = (
    "Voce e o Pablo, representante comercial da Code House. "
    "A Code House e uma empresa de desenvolvimento de software sob medida: "
    "criamos paginas institucionais, ERPs, CRMs e automacao de atendimento (chat). "
    "Voce fala com donos de clinicas, empresas e comercio local. "
    "Regras de tom: "
    "1) seja humano, natural, como uma conversa de WhatsApp real (frases curtas, "
    "sem jargao de vendedor, sem 'Prezado(a)'); "
    "2) sempre se apresente como Pablo da Code House na PRIMEIRA mensagem; "
    "3) mostre que estudou a dor do cliente (cite algo especifico do segmento/empresa); "
    "4) seja consultivo, nao empurrador; "
    "5) se o cliente demonstrar interesse ou pedir horario, envie o link de agendamento; "
    "6) se pedir para parar, respeite e agradeca; "
    "7) nunca prometa valores sem confirmar; "
    "8) mantenha o fio da conversa (use o historico)."
)

HISTORY_LIMIT = 8  # ultimas N mensagens como contexto


def _history_text(db, lead_id: int) -> str:
    with db.session() as s:
        msgs = (
            s.query(Message)
            .filter_by(lead_id=lead_id)
            .order_by(Message.id)
            .limit(HISTORY_LIMIT * 2)
            .all()
        )
    lines = []
    for m in msgs:
        who = "Cliente" if m.direcao == "in" else "Pablo"
        lines.append(f"{who}: {m.conteudo}")
    return "\n".join(lines)


def _dores_text(lead: Lead, enr: Enrichment | None) -> str:
    partes = [f"Empresa: {lead.empresa}", f"Segmento: {lead.segmento}"]
    if lead.site:
        partes.append(f"Site: {lead.site}")
    if lead.rede_social:
        partes.append(f"Rede: {lead.rede_social}")
    if enr:
        partes.append(f"Dores mapeadas: {enr.dor_estimada or 'nao mapeada'}")
        partes.append(f"Ja tem sistema: {'sim' if enr.tem_sistema else 'nao'}")
    return "\n".join(partes)


def first_contact(db, lead: Lead, enr: Enrichment | None,
                  base_url: str, api_key: str, model: str,
                  schedule_url: str = "") -> str:
    """1a mensagem: apresentacao Pablo + Code House + dor do lead."""
    system = PERSONA + (
        "\n\nEsta e a PRIMEIRA mensagem. Apresente-se como Pablo da Code House, "
        "explique brevemente o que fazemos (software sob medida: paginas, ERPs, "
        "CRMs, automacao), e relacione com a dor do cliente. No maximo 4 frases. "
        "Sem link ainda."
    )
    user = _dores_text(lead, enr)
    out = chat_completion(base_url, api_key, model, system, user, timeout=60)
    return humanize(out.strip())


def reply(db, lead: Lead, enr: Enrichment | None,
          customer_text: str, base_url: str, api_key: str, model: str,
          schedule_url: str = "") -> str:
    """Resposta do Pablo mantendo o fio da conversa.

    Se o cliente quer horario/agenda, o Pablo envia o link no fim.
    """
    history = _history_text(db, lead.id)
    system = PERSONA + (
        "\n\nResponda como Pablo, mantendo o fio da conversa. "
        "Se o cliente pediu horario, demonstracao ou demonstrou interesse claro, "
        "Termine a mensagem com a linha: LINK_AGENDA: <url> (use o schedule_url). "
        "Caso contrario, continue a conversa naturalmente sem link."
    )
    user = (
        f"{_dores_text(lead, enr)}\n\n"
        f"Historico da conversa:\n{history}\n\n"
        f"Cliente acabou de dizer: {customer_text}\n\n"
        f"schedule_url: {schedule_url or '<sem link>'}"
    )
    out = chat_completion(base_url, api_key, model, system, user, timeout=60)
    return humanize(out.strip())
