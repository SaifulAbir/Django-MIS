#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE="sknf.settings"
cat <<EOF | python manage.py shell
from django.db import connection
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from accounts.models import User

cursor = connection.cursor()
cursor.execute('update users set username=email;')
EOF