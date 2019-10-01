from sknf.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sknfdb',
        'USER': 'root',
        'PASSWORD': 'Ish1234#',
        'HOST': 'sknf-db.cae55b7vy4vo.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
