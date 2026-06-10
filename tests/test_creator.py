"""
Tests unitaires pour le module creator.

On teste la logique pure sans interagir avec le terminal.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from mission_creator import MissionConfig, creer_mission


@pytest.fixture
def destination(tmp_path: Path) -> Path:
    """Dossier temporaire fourni par pytest (nettoyé automatiquement)."""
    return tmp_path


def _config(nom: str, destination: Path) -> MissionConfig:
    return MissionConfig(
        nom=nom,
        destination=destination,
        date=datetime.now().strftime("%Y-%m-%d"),
    )


class TestCreerMission:

    def test_cree_dossier_racine(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        assert result.chemin.exists()
        assert result.chemin.is_dir()

    def test_prefixe_date(self, destination: Path) -> None:
        today = datetime.now().strftime("%Y-%m-%d")
        result = creer_mission(_config("TestMission", destination))
        assert result.chemin.name.startswith(today)

    def test_remplace_espaces_par_underscores(self, destination: Path) -> None:
        result = creer_mission(_config("Logo Refonte Client", destination))
        assert "Logo_Refonte_Client" in result.chemin.name

    def test_sous_dossiers_motion_design_crees(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        assert result.nb_dossiers > 0
        # Dossiers principaux
        assert (result.chemin / "00_ADMIN").is_dir()
        assert (result.chemin / "01_PREPROD").is_dir()
        assert (result.chemin / "02_ASSETS").is_dir()
        assert (result.chemin / "03_PROD").is_dir()
        assert (result.chemin / "04_REVIEW").is_dir()
        assert (result.chemin / "05_EXPORTS").is_dir()

    def test_sous_dossiers_assets_sources(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        # Les dossiers _Sources doivent exister pour protéger les originaux
        assert (result.chemin / "02_ASSETS" / "Images" / "_Sources").is_dir()
        assert (result.chemin / "02_ASSETS" / "Videos" / "_Sources").is_dir()

    def test_structure_review(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        assert (result.chemin / "04_REVIEW" / "V01").is_dir()
        assert (result.chemin / "04_REVIEW" / "V_FINAL").is_dir()

    def test_structure_exports_reseaux_sociaux(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        assert (result.chemin / "05_EXPORTS" / "Reseaux_Sociaux" / "Story_9x16").is_dir()
        assert (result.chemin / "05_EXPORTS" / "Reseaux_Sociaux" / "Feed_1x1").is_dir()

    def test_readme_racine_cree(self, destination: Path) -> None:
        result = creer_mission(_config("TestMission", destination))
        readme = result.chemin / "README.md"
        assert readme.exists()
        assert "TestMission" in readme.read_text(encoding="utf-8")

    def test_readme_contient_date(self, destination: Path) -> None:
        today = datetime.now().strftime("%Y-%m-%d")
        result = creer_mission(_config("TestMission", destination))
        readme = result.chemin / "README.md"
        assert today in readme.read_text(encoding="utf-8")

    def test_erreur_si_dossier_existant(self, destination: Path) -> None:
        config = _config("DoubleMission", destination)
        creer_mission(config)
        with pytest.raises(FileExistsError):
            creer_mission(config)

    def test_erreur_si_destination_inexistante(self, tmp_path: Path) -> None:
        faux_chemin = tmp_path / "nexiste_pas"
        with pytest.raises(FileNotFoundError):
            creer_mission(_config("TestMission", faux_chemin))
