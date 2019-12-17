from sknf.settings import *

DEBUG=False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = '/var/www/sknf_static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sknf',
        'USER': 'root',
        'PASSWORD': 'Ish1234#',
        'HOST': 'sknf-db.cae55b7vy4vo.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
