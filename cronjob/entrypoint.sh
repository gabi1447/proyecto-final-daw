#!/bin/sh
set -e

# Make container environment variables available to cron jobs.
printenv > /etc/environment

python3 /app/cronjob.py
exec cron -f
