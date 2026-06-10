#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  mission-creator.command
#  Double-clique sur ce fichier depuis le Finder pour lancer
#  le générateur de mission sans ouvrir le terminal manuellement.
# ─────────────────────────────────────────────────────────────

# Chemin absolu vers le dossier du projet
# 👉 Modifie cette ligne avec le vrai chemin sur ta machine
PROJET="$HOME/Documents/1_WORKS/mission_creator"

# Active le venv et lance le script
source "$PROJET/.venv/bin/activate"
mission-creator

# Garde le terminal ouvert après exécution pour voir le résultat
echo ""
echo "Appuie sur Entrée pour fermer..."
read
