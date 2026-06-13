#!/bin/bash
# Creates a weekly note directly in contents/weekly/
# Usage: bash new-weekly.sh

WEEKLY_DIR="/Volumes/4tb/2026-6/pirahansiah.github.io/contents/weekly"
YEAR=$(date +%Y)
MONTH=$(date +%b)
WEEK=$(date +%V)
FILENAME="${YEAR}-${MONTH}-W${WEEK}.md"
FILEPATH="${WEEKLY_DIR}/${FILENAME}"

if [ -f "$FILEPATH" ]; then
  echo "Already exists: $FILEPATH"
  exit 0
fi

cat > "$FILEPATH" << EOF
---
layout: farshid_default
title: "${YEAR}-${MONTH}-W${WEEK}"
tags: weekly pkm
categories: pulse
links: https://pirahansiah.github.io/
references: system-design, knowledge-graph
related: offering, growth-model
backlinks: /contents/pkm/atlas/knowledge-graph.md
created: "$(date +%Y-%m-%d)"
---

# ${YEAR} ${MONTH} — Week ${WEEK}

## Highlights
- 

## Tasks
- [ ] 

## Notes
- 

## Next Week
- 
EOF

echo "Created: $FILEPATH"
