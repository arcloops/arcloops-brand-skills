#!/usr/bin/env bash
# Builds arcloops-brand.zip for upload in Claude (Settings > Capabilities > Skills).
set -euo pipefail
cd "$(dirname "$0")/skills"
rm -f ../arcloops-brand.zip
zip -rq ../arcloops-brand.zip arcloops-brand -x "*.DS_Store"
echo "Built $(cd .. && pwd)/arcloops-brand.zip"
