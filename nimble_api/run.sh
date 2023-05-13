#!/usr/bin/env bash
cd /webapps/nimble_api/
pip3 install -r requirements.txt
export DJANGO_SETTINGS_MODULE="nimble.settings"
python3 manage.py migrate --noinput
systemctl restart api
systemctl restart nginx
