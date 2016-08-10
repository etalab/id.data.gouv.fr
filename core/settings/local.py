from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

ALLOWED_HOSTS = ['data.gouv.dev', 'data.gouv.dev:7000',
'http://data.gouv.dev', 'http://data.gouv.dev:7000']

SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
