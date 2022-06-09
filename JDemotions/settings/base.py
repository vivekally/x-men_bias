import os

from configurations import Configuration

from JDemotions.settings.logger_settings import LoggerSettingsMixin


class Base(LoggerSettingsMixin, Configuration):
    """
    Base configuration is the default configuration.
    This has all the essential keys.
    Inherit to make changes for production, development and staging.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition
    INSTALLED_APPS = [
        # Django Basic Apps
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Django-origin-trail

        'rest_framework',
        'JDemotions.apps.diversity_prediction'
    ]

    MIDDLEWARE = [
        # Django basic middleware
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        # Django-origin-trail

        # static files
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    ROOT_URLCONF = 'JDemotions.urls'

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

    WSGI_APPLICATION = 'JDemotions.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/
    SETTINGS_DIR = os.path.join(os.path.dirname(__file__), '..')
    PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir))

    STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        STATIC_PATH,
    )
    # STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(PROJECT_PATH, "../static/")
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Django-origin-trail

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }
