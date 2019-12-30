#!/usr/bin/env bash
cd /home/ubuntu/projectsknf/
source venv/bin/activate
export DJANGO_SETTINGS_MODULE="sknf.settings-aws"
#python manage.py runserver 0:8000&
#echo $!>PID
python manage.py runserver 0:8000 > sknf.log
