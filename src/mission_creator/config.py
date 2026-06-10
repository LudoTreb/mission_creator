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
#  TYPE 1 — MOTION DESIGN
# ══════════════════════════════════════════════════════════════════

STRUCTURE_MOTION: dict[str, dict] = {

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

README_CONTENT_MOTION: dict[str, str] = {

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

    "04_REVIEW": (
        "## Review\n\n"
        "Archiver chaque version envoyée au client dans son propre sous-dossier.\n\n"
        "- Nommer les fichiers avec la date : `{nom_mission}_V01_2026-01-15.mp4`\n"
        "- `V_FINAL` = version validée par le client. Ne plus y toucher après validation.\n"
    ),

    "05_EXPORTS": (
        "## Exports\n\n"
        "Livrables finaux prêts à livrer.\n\n"
        "- `Master/ProRes` → archivage haute qualité\n"
        "- `Master/H264_Web` → diffusion web générique\n"
        "- `Reseaux_Sociaux/` → un sous-dossier par format\n"
    ),

}


# ══════════════════════════════════════════════════════════════════
#  TYPE 2 — GRAPHISME / PRINT
# ══════════════════════════════════════════════════════════════════

STRUCTURE_GRAPHISME: dict[str, dict] = {

    # ── Administration & suivi client ─────────────────────────────
    "00_ADMIN": {
        "Brief":            {},   # brief client, cahier des charges
        "Devis_Contrat":    {},   # devis signé, contrat
        "Factures":         {},   # factures émises
        "Echanges":         {},   # captures d'écran d'emails, retours importants
    },

    # ── Préproduction ─────────────────────────────────────────────
    "01_PREPROD": {
        "References":       {},   # moodboard, inspirations visuelles
        "Moodboard":        {},   # planche d'ambiance couleurs / typo / style
        "Croquis":          {},   # esquisses, rough, schémas de mise en page
        "Textes_Contenus":  {},   # textes validés, contenus à intégrer
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
        "Illustrations": {
            "_Sources":     {},   # fichiers Ai / Procreate / Figma originaux
            "_Exports":     {},   # PNG, SVG exportés pour intégration
        },
    },

    # ── Production : fichiers de travail par logiciel ─────────────
    "03_PROD": {
        "Photoshop":        {},   # retouches, photomontages, compositions
        "Illustrator":      {},   # illustrations vectorielles, logos, icônes
        "InDesign":         {},   # mise en page (affiche, newsletter, presse)
        "Figma":            {},   # maquettes UI, carrousels, formats digitaux
    },

    # ── Review : versions envoyées au client ──────────────────────
    "04_REVIEW": {
        "V01":              {},   # première proposition
        "V02":              {},
        "V_FINAL":          {},   # version validée par le client — NE PAS MODIFIER
    },

    # ── Exports : livrables finaux par format ─────────────────────
    "05_EXPORTS": {
        "Print": {
            "PDF_HD":       {},   # PDF haute définition pour impression
            "PDF_BAT":      {},   # bon à tirer validé
        },
        "Numerique": {
            "JPEG_Web":     {},   # JPEG optimisé pour web
            "PNG_Transparent": {},  # PNG avec transparence
        },
        "Reseaux_Sociaux": {
            "Story_9x16":   {},
            "Feed_1x1":     {},
            "Carrousel":    {},
        },
    },

}

README_CONTENT_GRAPHISME: dict[str, str] = {

    "": (
        "# {nom_mission}\n\n"
        "Projet démarré le {date}.\n\n"
        "---\n\n"
        "## Structure\n\n"
        "| Dossier | Contenu |\n"
        "|---|---|\n"
        "| `00_ADMIN` | Brief, devis, factures, échanges client |\n"
        "| `01_PREPROD` | Références, moodboard, croquis, textes |\n"
        "| `02_ASSETS` | Toutes les sources (brand, images, illustrations) |\n"
        "| `03_PROD` | Fichiers de travail Photoshop, Illustrator, InDesign, Figma |\n"
        "| `04_REVIEW` | Versions envoyées au client |\n"
        "| `05_EXPORTS` | Livrables finaux (print, web, réseaux sociaux) |\n\n"
        "> Les dossiers préfixés `_Sources` contiennent les fichiers originaux bruts.\n"
        "> **Ne jamais les modifier directement.**\n"
    ),

    "04_REVIEW": (
        "## Review\n\n"
        "Archiver chaque version envoyée au client dans son propre sous-dossier.\n\n"
        "- Nommer les fichiers avec la date : `{nom_mission}_V01_2026-01-15.pdf`\n"
        "- `V_FINAL` = version validée par le client. Ne plus y toucher après validation.\n"
    ),

    "05_EXPORTS": (
        "## Exports\n\n"
        "Livrables finaux prêts à livrer.\n\n"
        "- `Print/PDF_HD` → impression haute qualité\n"
        "- `Print/PDF_BAT` → bon à tirer signé\n"
        "- `Numerique/` → formats web optimisés\n"
        "- `Reseaux_Sociaux/` → un sous-dossier par format\n"
    ),

}


# ══════════════════════════════════════════════════════════════════
#  INDEX — associe chaque type à ses données
# ══════════════════════════════════════════════════════════════════

TYPES_PROJET: dict[str, dict] = {
    "motion":     {"structure": STRUCTURE_MOTION,    "readme": README_CONTENT_MOTION},
    "graphisme":  {"structure": STRUCTURE_GRAPHISME,  "readme": README_CONTENT_GRAPHISME},
}
