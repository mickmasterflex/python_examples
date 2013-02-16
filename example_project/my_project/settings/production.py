from __init__ import *

### DATABASES {{{1
###############################################################################
DATABASES = {
    'default': {
        'NAME': 'speakeasy',
        'ENGINE': 'django_hstore.postgresql_psycopg2',
        'USER': 'speakeasy',
        'HOST': '',
        'PASSWORD': '',
        },
    'read': {
        'NAME': 'speakeasy',
        'ENGINE': 'django_hstore.postgresql_psycopg2',
        'USER': 'speakeasy',
        'HOST': '',
        'PASSWORD': '',
        },
    }
# }}}

STATIC_ROOT = '/var/www/sites/speakeasyspot.com/speakeasy/static/'
COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less',   'lessc {infile} {outfile}'),
)

### local_settings import {{{1
try:
    from production_local import *
except ImportError:
    pass
# }}}


# vim: foldmethod=marker
