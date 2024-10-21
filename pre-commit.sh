#!/bin/bash

SOURCE_HOOK="./scripts/pre-commit"
DEST_HOOK="$(git rev-parse --show-toplevel)/.git/hooks/pre-commit"

if [ ! -f "$SOURCE_HOOK" ]; then
    echo "Error: Custom pre-commit hook not found at $SOURCE_HOOK"
    exit 1
fi

if [ -f "$DEST_HOOK" ]; then
    echo "Error: Custom pre-commit hook already installed."
    exit 1
fi

cp "$SOURCE_HOOK" "$DEST_HOOK"
chmod +x "$DEST_HOOK"
echo "Pre-commit hook has been successfully installed."

