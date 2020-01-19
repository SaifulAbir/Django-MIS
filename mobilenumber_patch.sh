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


for h in HeadmasterProfile.objects.all():
    userobj=User.objects.get(pk=h.user_id)
    mobile=userobj.email
    h.mobile=''
    h.save()
    h.mobile=mobile
    h.save()

for l in SkLeaderProfile.objects.all():
    userobj=User.objects.get(pk=l.user_id)
    mobile=userobj.email
    l.mobile=''
    l.save()
    l.mobile=mobile
    l.save()

for m in SkMemberProfile.objects.all():
    userobj=User.objects.get(pk=m.user_id)
    mobile=userobj.email
    m.mobile=''
    m.save()
    m.mobile=mobile
    m.save()


EOF