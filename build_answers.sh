#!/usr/bin/env bash
set -e

# Détecter le binaire sphinx-build (local venv ou système)
if [ -f "./myvenv/bin/sphinx-build" ]; then
    SPHINXBUILD="./myvenv/bin/sphinx-build"
elif [ -f "./.venv/bin/sphinx-build" ]; then
    SPHINXBUILD="./.venv/bin/sphinx-build"
elif command -v sphinx-build >/dev/null 2>&1; then
    SPHINXBUILD="sphinx-build"
else
    echo "Erreur : sphinx-build introuvable." >&2
    exit 1
fi

BUILDDIR="build"
OUTPUTDIR="$BUILDDIR/html_answers"
DOCTREES="$BUILDDIR/doctrees_answers"

OPEN_BROWSER=false
SPHINX_EXTRA_ARGS=()

for arg in "$@"; do
    case "$arg" in
        --open|-o)
            OPEN_BROWSER=true
            ;;
        *)
            SPHINX_EXTRA_ARGS+=("$arg")
            ;;
    esac
done

echo "Génération du site avec réponses dans $OUTPUTDIR..."
"$SPHINXBUILD" -b html -D show_answers=1 -d "$DOCTREES" source "$OUTPUTDIR" "${SPHINX_EXTRA_ARGS[@]}"

echo ""
echo "Site avec réponses généré avec succès !"
echo "Fichier principal : $OUTPUTDIR/index.html"

if [ "$OPEN_BROWSER" = true ]; then
    if command -v open >/dev/null 2>&1; then
        open "$OUTPUTDIR/index.html"
    elif command -v xdg-open >/dev/null 2>&1; then
        xdg-open "$OUTPUTDIR/index.html"
    fi
else
    echo "Pour l'ouvrir dans votre navigateur : open $OUTPUTDIR/index.html"
fi
