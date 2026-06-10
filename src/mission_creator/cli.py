"""
Interface en ligne de commande.

Ce module gère uniquement les interactions avec l'utilisateur
(questions, affichage). La logique métier reste dans creator.py.

👉 Pour changer le dossier par défaut : modifier DEFAULT_DESTINATION ci-dessous.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

from .creator import MissionConfig, creer_mission


# ══════════════════════════════════════════════════════════════════
#  PARAMÈTRES — modifier ici si besoin
# ══════════════════════════════════════════════════════════════════

# Dossier proposé par défaut quand tu appuies sur Entrée sans rien saisir.
# Path.home() = ton dossier utilisateur (~)
DEFAULT_DESTINATION = Path.home() / "Documents" / "1_WORKS" / "Freelance"


# ══════════════════════════════════════════════════════════════════


def main() -> None:
    """Point d'entrée de la commande `mission-creator`."""
    print("\n🎨  Mission Creator\n" + "─" * 38)

    type_projet = _saisir_type()
    nom = _saisir_nom()
    destination = _saisir_destination()
    date = datetime.now().strftime("%Y-%m-%d")

    config = MissionConfig(nom=nom, destination=destination, date=date, type_projet=type_projet)

    try:
        result = creer_mission(config)
    except FileExistsError as e:
        _erreur(str(e))
    except FileNotFoundError as e:
        _erreur(str(e))

    print(f"\n  ✅  Mission créée : {result.chemin}")
    print(f"      {result.nb_dossiers} dossiers générés.\n")


# ── Helpers I/O ──────────────────────────────────────────────────


def _saisir_type() -> str:
    """Demande le type de projet et retourne la clé correspondante."""
    print("\nType de projet :")
    print("  1. Motion Design")
    print("  2. Graphisme / Print")
    while True:
        choix = input("Choix [1/2] : ").strip()
        if choix == "1":
            return "motion"
        if choix == "2":
            return "graphisme"
        print("  ⚠  Saisir 1 ou 2.")


def _saisir_nom() -> str:
    """Demande le nom de la mission jusqu'à obtenir une valeur non vide."""
    while True:
        nom = input("Nom de la mission (ex: Nike_Campagne_Ete) : ").strip()
        if nom:
            return nom
        print("  ⚠  Le nom ne peut pas être vide.")


def _saisir_destination() -> Path:
    """Demande le dossier parent, avec DEFAULT_DESTINATION comme valeur par défaut."""
    choix = input(f"Dossier parent [{DEFAULT_DESTINATION}] : ").strip()
    return Path(choix) if choix else DEFAULT_DESTINATION


def _erreur(message: str) -> None:
    """Affiche un message d'erreur et quitte."""
    print(f"\n  ❌  {message}\n")
    sys.exit(1)
