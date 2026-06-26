#!/usr/bin/env bash
set -euo pipefail

mkdir -p notes from_scratch notebooks paper_summaries

touch notes/.gitkeep
touch from_scratch/.gitkeep
touch notebooks/.gitkeep
touch paper_summaries/.gitkeep

echo "Created project folders:"
echo " notes/"
echo " from_scratch/"
echo " notebooks/"
echo " paper_summaries/"
