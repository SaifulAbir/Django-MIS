#!/usr/bin/env bash
cd /sknfproject
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requirements.txt
python manage.py migrate
cat <<EOF | python manage.py shell
export DJANGO_SETTINGS_MODULE="sknf.settings-aws"
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin').exists():
   user = User.objects.create_superuser('admin', '123')
   user.user_type = 1
   user.first_name = 'Admin'
   user.save()
EOF
python manage.py runserver 0:80&
echo $!>PID
