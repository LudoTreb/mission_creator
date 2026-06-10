"""
╔══════════════════════════════════════════════════════════════════╗
║                        config.py                                 ║
║                                                                  ║
║  C'est LE fichier à modifier pour personnaliser le projet.       ║
║  Les autres fichiers (creator.py, cli.py) n'ont pas besoin       ║
║  d'être touchés pour changer la structure des dossiers.          ║
╚══════════════════════════════════════════════════════════════════╝

COMMENT MODIFIER LA STRUCTURE :
  - Ajouter un dossier    → ajouter une clé dans le bon dict
  - Supprimer un dossier  → supprimer la ligne correspondante
  - Renommer un dossier   → changer la clé (ex: "05_EXPORTS" → "05_LIVRABLES")
  - Ajouter un sous-dossier → ajouter une clé dans le dict parent

FORMAT :
  "NOM_DOSSIER": {}                    ← dossier vide (feuille)
  "NOM_DOSSIER": { "SOUS": {}, ... }   ← dossier avec sous-dossiers
"""

from __future__ import annotations


# ══════════════════════════════════════════════════════════════════
#  STRUCTURE DES DOSSIERS
#  Modifie uniquement cette section pour changer l'arborescence.
# ══════════════════════════════════════════════════════════════════

STRUCTURE: dict[str, dict] = {

    # ── Administration & suivi client ─────────────────────────────
    "00_ADMIN": {
        "Brief":            {},   # brief client, cahier des charges
        "Devis_Contrat":    {},   # devis signé, contrat
        "Factures":         {},   # factures émises
        "Echanges":         {},   # captures d'écran d'emails, retours importants
    },

    # ── Préproduction : avant de toucher After Effects ────────────
    "01_PREPROD": {
        "References":       {},   # moodboard, références visuelles et motion
        "Storyboard":       {},   # storyboard dessiné ou numérique
        "Animatique":       {},   # version timing avant prod
        "Scripts_Textes":   {},   # voiceover validé, textes définitifs
    },

    # ── Assets : toutes les sources organisées par type ───────────
    "02_ASSETS": {
        "Brand": {
            "_Charte":      {},   # guidelines, PDF de charte fournis par le client
            "_Logos":       {},   # logos vectoriels (AI, SVG, EPS)
            "_Fonts":       {},   # copies locales des polices du projet
        },
        "Images": {
            "_Sources":     {},   # fichiers originaux bruts — NE JAMAIS MODIFIER
            "_Ready":       {},   # recadrées, retouchées, prêtes à l'emploi
        },
        "Videos": {
            "_Sources":     {},   # rushes originaux — NE JAMAIS MODIFIER
            "_Ready":       {},   # clips retravaillés, prêts à l'import
        },
        "Audio": {
            "Musiques":     {},
            "SFX":          {},   # effets sonores
            "Voiceover":    {},   # fichiers voix off
        },
        "Illustrations": {
            "_Sources":     {},   # fichiers Ai / Figma originaux
            "_Exports":     {},   # SVG, PNG exportés pour After Effects
        },
    },

    # ── Production : fichiers de travail par logiciel ─────────────
    "03_PROD": {
        "AfterEffects": {
            "footage":      {},   # médias liés au projet AE (chemin relatif)
        },
        "C4D_Blender": {
            "Scenes":       {},   # fichiers de scène 3D
            "Textures":     {},   # textures et matériaux
            "Renders":      {},   # sorties PNG / EXR des renders 3D
        },
        "Premiere_DaVinci": {},   # projet de montage et étalonnage final
        "Illustrator_Figma": {},  # assets graphiques en cours de création
    },

    # ── Review : versions envoyées au client ──────────────────────
    "04_REVIEW": {
        "V01":              {},   # première version (H264 basse déf + timecode)
        "V02":              {},
        "V_FINAL":          {},   # version validée par le client — NE PAS MODIFIER
    },

    # ── Exports : livrables finaux par format ─────────────────────
    #  👉 Pour renommer ce dossier : changer "05_EXPORTS" ci-dessous
    "05_EXPORTS": {
        "Master": {
            "ProRes":       {},   # ProRes 422 / 4444 pour archivage
            "H264_Web":     {},   # H264 pour diffusion web
        },
        "Reseaux_Sociaux": {
            "Story_9x16":   {},
            "Feed_1x1":     {},
            "Banner_16x9":  {},
        },
        "Assets_Statiques": {},   # frames clés, vignettes, formats print
        "GIF_WEBM":         {},   # formats animés légers pour web
    },

}


# ══════════════════════════════════════════════════════════════════
#  README — notes d'orientation dans les dossiers clés
#  Clé = chemin relatif depuis la racine ("" = racine du projet).
#  {nom_mission} et {date} sont remplacés automatiquement.
# ══════════════════════════════════════════════════════════════════

README_CONTENT: dict[str, str] = {

    # Racine du projet
    "": (
        "# {nom_mission}\n\n"
        "Projet démarré le {date}.\n\n"
        "---\n\n"
        "## Structure\n\n"
        "| Dossier | Contenu |\n"
        "|---|---|\n"
        "| `00_ADMIN` | Brief, devis, factures, échanges client |\n"
        "| `01_PREPROD` | Références, storyboard, animatique, scripts |\n"
        "| `02_ASSETS` | Toutes les sources (brand, images, vidéos, audio) |\n"
        "| `03_PROD` | Fichiers de travail AE, C4D, Premiere… |\n"
        "| `04_REVIEW` | Versions envoyées au client |\n"
        "| `05_EXPORTS` | Livrables finaux par format |\n\n"
        "> Les dossiers préfixés `_Sources` contiennent les fichiers originaux bruts.\n"
        "> **Ne jamais les modifier directement.**\n"
    ),

    # Rappel dans le dossier Review
    "04_REVIEW": (
        "## Review\n\n"
        "Archiver chaque version envoyée au client dans son propre sous-dossier.\n\n"
        "- Nommer les fichiers avec la date : `{nom_mission}_V01_2026-01-15.mp4`\n"
        "- `V_FINAL` = version validée par le client. Ne plus y toucher après validation.\n"
    ),

    # Rappel dans le dossier Exports
    "05_EXPORTS": (
        "## Exports\n\n"
        "Livrables finaux prêts à livrer.\n\n"
        "- `Master/ProRes` → archivage haute qualité\n"
        "- `Master/H264_Web` → diffusion web générique\n"
        "- `Reseaux_Sociaux/` → un sous-dossier par format\n"
    ),

}
