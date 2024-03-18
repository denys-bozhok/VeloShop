from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-44f^7q69rd8ri&0-hiwmak^@4h4xb3nz+*)vf16&%lu9c9wph&'
DEBUG = True
ALLOWED_HOSTS = []
DOMAIN_NAME = 'http://127.0.0.1:8000'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',

    'sass_processor',
    'compressor',
    'queryset_sequence',
    'debug_toolbar',

    'users',
    'app',
    'products',
    'carts',
    'orders',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'livereload.middleware.LiveReloadScript',
    'allauth.account.middleware.AccountMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'Store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carts.context_processors.get_all_carts',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'Store.wsgi.application'

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'veloshop_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / STATIC_URL
SASS_PROCESSOR_ROOT = BASE_DIR / STATIC_URL

COMPRESS_ROOT = BASE_DIR / STATIC_URL

MEDIA_DIR = BASE_DIR / 'media'
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    ]


LOGIN_REDIRECT_URL = 'index'

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': [
            'user',
        ],
    }
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'denys.already@gmail.com'
EMAIL_HOST_PASSWORD = 'soht vqyk chgm iutf'
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'denys.already@gmail.com'

INTERNAL_IPS = [
    '127.0.0.1',
]



# whsec_1b6e22c1f5ed9278adacdc7af2c60f08d0caa79d3259703de17aad7f05
# 89eeaf1fdfc805a77e02 gh
# d5d7e270dbe83a8c33318e8c6e9b523b53bceff5 gh
STRIPE_PUBLIC_KEY = 'pk_test_51OvVTFA382WBKVuqPEz5Haa5EDPmpqurO6IlCRHnLuvbCA00i18psYhKA1DKALCXQFcSLCUtITCricj4tQxpdRJp00RpdYZkgk'
STRIPE_SECRET_KEY = 'sk_test_51OvVTFA382WBKVuqrCGkH6VQcDPlBiIYk2kBn7PLYMWVtUhLgb4LwVN0W8LBAP6scnwp2OCLZ5O4IaeQyEgLVjN300kLwjBJwB'
STRIPE_WEBHOOK_SECRET = 'whsec_1b6e22c1f5ed9278adacdc7af2c60f08d0caa79d3259703de17aad7f05'