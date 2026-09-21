#!/usr/bin/env bash
set -o errexit

PYTHON_CMD="python"
PIP_CMD="pip"

if ! command -v pip &> /dev/null; then
    if [ -f "./venv/bin/pip" ]; then
        PIP_CMD="./venv/bin/pip"
        PYTHON_CMD="./venv/bin/python"
    elif command -v python3 &> /dev/null; then
        PIP_CMD="python3 -m pip"
        PYTHON_CMD="python3"
    fi
fi

echo "==> Installing Python dependencies..."
$PIP_CMD install -r requirements.txt

echo "==> Collecting static files..."
$PYTHON_CMD manage.py collectstatic --noinput

echo "==> Running database migrations..."
$PYTHON_CMD manage.py migrate
