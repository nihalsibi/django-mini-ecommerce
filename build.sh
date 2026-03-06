#!/usr/bin/env bash
set -o errexit

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python manage.py migrate --noinput

# Run collectstatic only when STATIC_ROOT is configured.
if python manage.py shell -c "from django.conf import settings; import sys; sys.exit(0 if getattr(settings, 'STATIC_ROOT', None) else 1)"; then
  python manage.py collectstatic --noinput
fi
