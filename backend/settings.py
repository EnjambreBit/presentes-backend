import os
import dj_database_url
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EN_MODO_TESTS = 'test' in str(sys.argv) or 'migrate' in str(sys.argv)
SECRET_KEY = '&h8i_90-25+@k)#*+7*oqb63+018hlwoe&y1#oav#wj8)nikb*'

FRONTEND_URL = os.environ.get('FRONTEND_URL')
BACKEND_URL = os.environ.get('BACKEND_URL')

HOST_BACKEND = BACKEND_URL.replace("http://", "").replace("https://", "")

DEBUG = False

VERSION_NUMBER = "0.0.19"
ALLOWED_HOSTS = ['127.0.0.19', '127.0.0.190', 'localhost', 'localhost:4200', 'presentes.enjambrelab.space', 'presentes-backend.enjambrelab.space', '127.0.0.1', 'mapa.agenciapresentes.org', HOST_BACKEND]
CORS_ORIGIN_WHITELIST = ALLOWED_HOSTS

JSON_API_FORMAT_FIELD_NAMES = 'dasherize'
JSON_API_FORMAT_RELATION_KEYS = 'dasherize'
JSON_API_PLURALIZE_RELATION_TYPE = True
CORS_ORIGIN_ALLOW_ALL = False
APPEND_SLASH = False
DATETIME_FORMAT="%H"

if EN_MODO_TESTS:
    DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS = False
    DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS = False
    DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = False
else:
    DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django_filters',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'easyaudit',
    'rest_framework',
    'rest_framework.authtoken',
    'presentes'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


DATABASES = {
}

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default']['OPTIONS']['sslmode'] = 'disable'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'PAGE_SIZE': 500,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.environ.get('PRESENTES_MEDIA_ROOT', 'media_archivos_locales')
MEDIA_URL = '/media/'
