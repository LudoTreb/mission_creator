"""
Logique de création de la structure de dossiers.

Ce module ne fait pas d'I/O utilisateur : il reçoit des données
et crée les fichiers/dossiers. Facile à tester et à réutiliser.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import TYPES_PROJET


@dataclass
class MissionConfig:
    """Paramètres d'une nouvelle mission."""

    nom: str           # nom brut saisi par l'utilisateur
    destination: Path  # dossier parent où créer la mission
    date: str          # date au format YYYY-MM-DD
    type_projet: str   # "motion" ou "graphisme"


@dataclass
class MissionResult:
    """Résultat d'une création de mission."""

    chemin: Path      # chemin absolu du dossier créé
    nb_dossiers: int  # nombre de dossiers créés


def creer_mission(config: MissionConfig) -> MissionResult:
    """
    Point d'entrée principal : crée toute la structure de mission.

    Args:
        config: paramètres de la mission à créer.

    Returns:
        MissionResult avec le chemin créé et les statistiques.

    Raises:
        FileExistsError: si le dossier cible existe déjà.
        FileNotFoundError: si le dossier parent n'existe pas.
    """
    if not config.destination.exists():
        raise FileNotFoundError(f"Dossier parent introuvable : {config.destination}")

    nom_dossier = _sanitize(config.nom)
    dossier_mission = config.destination / f"{config.date}_{nom_dossier}"

    if dossier_mission.exists():
        raise FileExistsError(f"Ce dossier existe déjà : {dossier_mission}")

    type_data = TYPES_PROJET[config.type_projet]
    _creer_dossiers(dossier_mission, type_data["structure"])
    _creer_readmes(dossier_mission, config.nom, config.date, type_data["readme"])

    nb_dossiers = sum(1 for p in dossier_mission.rglob("*") if p.is_dir())
    return MissionResult(chemin=dossier_mission, nb_dossiers=nb_dossiers)


# ── Fonctions privées ────────────────────────────────────────────────────────


def _sanitize(nom: str) -> str:
    """Remplace les espaces par des underscores pour un nom de dossier propre."""
    return nom.strip().replace(" ", "_")


def _creer_dossiers(base: Path, structure: dict[str, dict]) -> None:
    """Crée récursivement tous les dossiers définis dans `structure`."""
    for nom, enfants in structure.items():
        dossier = base / nom
        dossier.mkdir(parents=True, exist_ok=True)
        if enfants:
            _creer_dossiers(dossier, enfants)


def _creer_readmes(base: Path, nom_mission: str, date: str, readme_content: dict[str, str]) -> None:
    """Dépose les fichiers README.md dans les dossiers configurés."""
    for sous_chemin, contenu in readme_content.items():
        chemin = (base / sous_chemin / "README.md") if sous_chemin else (base / "README.md")
        texte = contenu.format(nom_mission=nom_mission, date=date)
        chemin.write_text(texte, encoding="utf-8")
