from sknf.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sknf',
        'USER': 'root',
        'PASSWORD': 'Ish1234#',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
