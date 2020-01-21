#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE="sknf.settings"
cat <<EOF | python manage.py shell
from django.db import connection
from headmasters.models import HeadmasterProfile
from skleaders.models import SkLeaderProfile
from skmembers.models import SkMemberProfile
from accounts.models import User

for m in SkMemberProfile.objects.all():
    userobj=User.objects.get(pk=m.user_id)
    email= userobj.email
    first_name = userobj.first_name
    m.email=email
    m.name=first_name
    m.save()

EOF