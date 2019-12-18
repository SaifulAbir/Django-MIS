#!/usr/bin/env bash
cd /home/ubuntu/projectsknf/
source venv/bin/activate
python manage.py runserver 0:8000&
echo $!>PID
