cd /sknfproject
python check_db.py
python manage.py migrate
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin').exists():
   user = User.objects.create_superuser('email', 'pass')
   user.user_type = 1
   user.save()
EOF
python manage.py runserver 0:8000
