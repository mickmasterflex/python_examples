from __init__ import *

DEBUG = True
TEMPLATE_DEBUG = True

# disable automatic less compilation:
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = tuple()

DBINFO = {
    'ENGINE': 'django_hstore.postgresql_psycopg2',
    'NAME': 'speakeasy',
    'USER': 'speakeasy',
    'HOST': 'localhost',
    'PASSWORD': 'speakeasy',
}

for item in ('default', 'read'):
    DATABASES[item].update(DBINFO)

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
THUMBNAIL_DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'

ADMIN_MEDIA_PREFIX = '/media/admin-media/'
BROKER_URL = 'amqp://guest@localhost//'

### LOCAL {{{1
###############################################################################
try:
    from dev_local import *
except ImportError:
    pass
# }}}
