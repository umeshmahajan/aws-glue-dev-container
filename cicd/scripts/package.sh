#!/bin/bash
set -e

echo "Packaging Glue job..."

mkdir -p build

# Copy job scripts
cp src/jobs/*.py build/

# Zip dependencies (optional)
pip install -r requirements.txt -t build/

echo "Package complete"
