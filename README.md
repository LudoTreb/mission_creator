# Mission Creator 🎨

Générateur de structure de dossiers pour nouvelles missions graphiques.

## Installation

```bash
# 1. Cloner / télécharger le projet, puis se placer dedans
cd mission_creator

# 2. Créer et activer l'environnement virtuel
python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows

# 3. Installer le projet en mode développement
pip install -e ".[dev]"
```

## Utilisation

### Option A — Double-clic depuis le Finder (le plus simple)

1. Ouvre `mission-creator.command` dans un éditeur texte et vérifie que la ligne `PROJET` pointe bien vers ton dossier
2. Au premier lancement : clic droit → **Ouvrir** (pour contourner Gatekeeper macOS)
3. Ensuite : double-clic suffit

### Option B — Alias dans le terminal (le plus rapide)

Ajoute cette ligne à ton `~/.zshrc` :

```bash
alias mission="source $HOME/mission_creator/.venv/bin/activate && mission-creator"
```

Puis recharge :

```bash
source ~/.zshrc
```

Désormais tu tapes juste `mission` dans n'importe quel terminal.

### Option C — Terminal classique

```bash
cd mission_creator
source .venv/bin/activate
mission-creator
```

Le script demande :
- le **nom de la mission** (ex : `LogoRefonte_MaBoite`)
- le **dossier parent** où créer la mission (par défaut : Bureau)

Il génère un dossier préfixé par la date (`2026-06-10_LogoRefonte_MaBoite`) avec toute la structure.

## Structure générée

```
2026-06-10_NomMission/
├── 01_BRIEF/
│   ├── Cahier_des_charges/
│   └── Références_client/
├── 02_RECHERCHE/
│   ├── Moodboard/
│   ├── Benchmarks/
│   └── Inspirations/
├── 03_PRODUCTION/
│   ├── Polices/
│   ├── Couleurs/
│   ├── Icones_Illustrations/
│   ├── Images/
│   │   ├── Sources/
│   │   └── Recadrées/
│   └── Fichiers_de_travail/
│       ├── Brouillons/
│       └── En_cours/
├── 04_LIVRABLES/
│   ├── V1/
│   ├── V2/
│   └── Final/
│       ├── Pour_impression/
│       └── Pour_web/
├── 05_EXPORTS/
│   ├── PDF/
│   ├── JPG_PNG/
│   └── SVG/
└── 06_ADMIN/
    ├── Devis_Factures/
    ├── Contrats/
    └── Échanges_client/
```

## Personnalisation

Modifier le dictionnaire `STRUCTURE` dans `src/mission_creator/config.py` pour adapter l'arborescence à tes besoins.

## Développement

```bash
# Lancer les tests
pytest

# Vérifier le style du code
ruff check src/

# Formater le code
ruff format src/

# Vérifier les types
mypy src/
```

## Faire évoluer le projet

| Besoin | Fichier à modifier |
|--------|-------------------|
| Changer la structure des dossiers | `src/mission_creator/config.py` |
| Ajouter des questions à la saisie | `src/mission_creator/cli.py` |
| Modifier la logique de création | `src/mission_creator/creator.py` |
| Ajouter des tests | `tests/` |
