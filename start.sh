#!/usr/bin/env bash
source venv/bin/activate
pip3 install -r requirements.txt
python manage.py migrate
cat <<EOF | python3 manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
   user = User.objects.create_superuser('admin', 'admin@sknf.org', '123')
   user.user_type = 1
   user.first_name = 'Admin'
   user.save()
EOF
python manage.py runserver 0:8000
