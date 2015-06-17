
"""
Django settings for again_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from config import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gh#k2(o^6q*yx0_^1q2ve!w$a-8+f=p-j6_cktl88qo-o-m-e8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'social.apps.django_app.default',
    'django.contrib.comments',
    'blogs',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'pagedown',
    'datetimewidget',
    'djcelery',
    'kombu.transport.django',

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    "django.core.context_processors.request",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
 
    'social.backends.google.GooglePlusAuth',
    "allauth.account.auth_backends.AuthenticationBackend",
)


ROOT_URLCONF = 'again_blog.urls'

WSGI_APPLICATION = 'again_blog.wsgi.application'

# ROOT_URLCONF = 'djangoblog.urls'
# WSGI_APPLICATION = 'djangoblog.wsgi.application'

SITE_ID = 1
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
 
SOCIAL_AUTH_GITHUB_KEY = 'a5df02999dc298d69003'
SOCIAL_AUTH_GITHUB_SECRET = '9803a4c90163851d63f1b8a6f84086a87b1ef0cb'


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '830092256873-lv3koubj9142ic6e6sts3lk9paju5il5.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'HHbmtp8ia6owBw_qE_a8qVnq'



# 825147385460-ceilv3ntkndv08t6a47crnmq011vqcrj@developer.gserviceaccount.com

# SOCIAL_AUTH_GOOGLE_PLUS_KEY = '...'
# SOCIAL_AUTH_GOOGLE_PLUS_SECRET = '...'

SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'

SOCIALACCOUNT_AUTO_SIGNUP =True
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_PORT=587
# EMAIL_HOST_USER='cis.dev393'
# EMAIL_HOST_PASSWORD='cisin123'
# # EMAIL_HOST_PASSWORD='cisin@123'
# EMAIL_USE_TLS = True
# SKIP_SOUTH_TESTS = False
# EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'


EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'yogesh.p@cisinlabs.com'
EMAIL_HOST_PASSWORD = '8BFcYUPihPoYQkdIs7cqKw'
# EMAIL_USE_TLS = True
DEFAULT_EMAIL_FROM = "no-reply@cisinlabs.com"
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (TEMPLATE_PATH,)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True

BROKER_URL = "django://"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

import djcelery
djcelery.setup_loader()

