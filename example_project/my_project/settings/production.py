from __init__ import *

### DATABASES {{{1
###############################################################################
DATABASES = {
    'default': {
        'NAME': 'my_project',
        'ENGINE': 'django_hstore.postgresql_psycopg2',
        'USER': 'my_project',
        'HOST': '',
        'PASSWORD': '',
        },
    'read': {
        'NAME': 'my_project',
        'ENGINE': 'django_hstore.postgresql_psycopg2',
        'USER': 'my_projet',
        'HOST': '',
        'PASSWORD': '',
        },
    }
# }}}

STATIC_ROOT = '/var/www/sites/your_domain.com/my_project/static/'
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
