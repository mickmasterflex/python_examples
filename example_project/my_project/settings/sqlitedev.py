from speakeasy.settings.dev import *

USE_POSTGRESHSTORE = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, "speakeasy.db"),
    }
}

