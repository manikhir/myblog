from settings import *


import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}



SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')