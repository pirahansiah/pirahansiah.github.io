#!/bin/bash

# Jekyll build and serve script for local development

echo "[JEKYLL] Installing gems..."
bundle install

echo "[JEKYLL] Starting local server..."
echo "[JEKYLL] Open http://localhost:4000 in your browser"

bundle exec jekyll serve --host 0.0.0.0 --port 4000 --incremental --watch