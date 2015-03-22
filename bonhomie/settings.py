"""
Django settings for bonhomie project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w98oo*=1beb4j_xv9t(@db9((1%)iarw6ta=z^was2qr3!o1dl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

## BONHOMIE SETTINGS
BONHOMIE_TAGS = [
    ('bug', '#c0392b'),
    ('feature', '#27ae60'),
    ('experimental', '#f1c40f'),
    ('optimization', '#8e44ad'),
]
BONHOMIE_TITLE = 'Dimagi'
BONHOMIE_DESCRIPTION = 'Driving the future of innovation'

BOWER_COMPONENTS_ROOT = BASE_DIR + '/components/'

BOWER_INSTALLED_APPS = (
    'knockout',
    'underscore',
    'jquery#1.9',
    'moment',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'restless',
    'markdown_deux',
    'django_extensions',
    'pipeline',
    'djangobower',
    'bootstrap3',
    'github',
    'ui',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bonhomie.urls'

WSGI_APPLICATION = 'bonhomie.wsgi.application'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_FINDERS = (
    "djangobower.finders.BowerFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    "pipeline.finders.PipelineFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/',
    BASE_DIR + '/ui/templates/',
)

# PIPLINE CONFIG

PIPELINE_CSS = {
    'global': {
        'source_filenames': (
          'ui/css/variables.scss',
          'ui/css/global.scss',
        ),
        'output_filename': 'ui/css/global.css',
    },
}

PIPELINE_JS = {
    'bonhomie': {
        'source_filenames': (
            'ui/js/bonhomie.coffee',
        ),
        'output_filename': 'js/bonhomie.js',
    }
}

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'

PIPELINE_COMPILERS = (
  'pipeline.compilers.coffee.CoffeeScriptCompiler',
  'pipeline.compilers.sass.SASSCompiler',
)
