from sknf.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sknf',
        'USER': 'root',
        'PASSWORD': '@ish123#',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}
