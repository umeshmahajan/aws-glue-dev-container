#!/bin/bash
set -e

echo "Uploading artifacts to S3..."

aws s3 cp build/ s3://$S3_BUCKET/artifacts/ --recursive

echo "Upload complete"
