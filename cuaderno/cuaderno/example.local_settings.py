SECRET_KEY = ''

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': '',
      'USER': '',
      'PASSWORD': '',
      'HOST': '',
      'PORT': '',
  }
}

OWNCLOUD_STORAGE_OPTIONS = {
    'url': '',
    'user': '',
    'password': '',
    'root': '',
}
