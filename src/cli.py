"""CLI do agente CodeHouse (R8/R9).

Uso: python -m src.cli [--config config.yaml] [--limit N] [--dry-run]
Roda um ciclo de prospecção ponta a ponta e imprime o resumo (R10 audit log).
"""
from __future__ import annotations

import argparse
import sys

from src.config import Config
from src.db import Database
from src.orchestrator import ProspectingAgent


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="codehouse-agent")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    cfg = Config.load(args.config)
    if args.limit:
        cfg.prospecting.limit = args.limit
    if args.dry_run:
        cfg.dry_run = True

    db = Database(cfg.db_url)
    agent = ProspectingAgent(cfg, db)
    stats = agent.run_cycle()
    print("[CODEHOUSE] ciclo concluído:", stats.summary())
    return 0


if __name__ == "__main__":
    sys.exit(main())
