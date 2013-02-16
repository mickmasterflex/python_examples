import tempfile

from __init__ import *

DEBUG = True
TEMPLATE_DEBUG = True
TASTYPIE_FULL_DEBUG = True

# disable automatic less compilation:
COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = tuple()

ADMIN_MEDIA_PREFIX = '/media/admin-media/'
MEDIA_ROOT = tempfile.mkdtemp()
MEDIA_URL = '/test/media/'

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_speakeasy.sqlite3',
}
DATABASES['read'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'test_speakeasy.sqlite3',
}
USE_POSTGRESHSTORE = False

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
THUMBNAIL_DEFAULT_STORAGE = 'django.core.files.storage.FileSystemStorage'

INSTALLED_APPS += ('django_nose',)

### TESTING {{{1
###############################################################################

# Define configuration for testing with coverage output
TEST_RUNNER = 'speakeasy.tests.SpeakEasyTestSuiteRunner'
COVERAGE_MODULES = [
    # accounts
    'accounts.forms', 'accounts.mixins', 'accounts.models', 'accounts.utils',

    # common
    'common.mixins', 'common.models', 'common.utils',

    # payment
    'payment.authorize', 'payment.credit_card_handling', 'payment.empay',
    'payment.first_data.py', 'payment.first_data_gge4', 'payment.forms',
    'payment.models', 'payment.post_handling',
]

# The following apps won't be tested by the testrunner.
TEST_EXCLUDE = [
    'django',
    'south',
    'compressor',
    'easy_thumbnails',
]

### local_settings import {{{1
try:
    from test_local import *
except ImportError:
    pass
# }}}
