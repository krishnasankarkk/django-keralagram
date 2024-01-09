"""
Django settings for instagram project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import cloudinary
          
cloudinary.config( 
  cloud_name = "dinphrbeu", 
  api_key = "499557373191457", 
  api_secret = "TF323Kby0hXq3cHv771aWzX7DHk" 
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lv%9ja!e7+z#alt1sdd#12*zp-z=!4a+43apx=-01df25ef8hg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['keralagram.vercel.app', '127.0.0.1','.vercel.app', '.now.sh','localhost']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'channels',
    'tailwind',
    'cloudinary',
        
    'users',
    'settings',
    'posts',
    'notifications',
    'messenger',
    'followers',
    'explore',
    'theme',
    ]

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1"
]

NPM_BIN_PATH = "C:\\Program Files\\nodejs\\npm.cmd"

MIDDLEWARE = [
    # "django_browser_reload.middleware.BrowserReloadMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'instagram.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
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

WSGI_APPLICATION = 'instagram.wsgi.app'

ASGI_APPLICATION = 'instagram.asgi.app'
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        # "CONFIG": {
        #     "hosts": [("127.0.0.1", 6379)],
        # },
    },
}


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#live railway server
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': '5*edg*BB21GG52e*54a4E2FAb5Cf*65C',
        'HOST': 'monorail.proxy.rlwy.net',  # Set to the hostname where your database is running, typically 'localhost'.
        'PORT': '41251',  # Leave empty to use the default PostgreSQL port (5432).
    }
}

# live render server
# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'keralagram',
#         'USER': 'krishna',
#         'PASSWORD': 'FvoIfuSMLEu7X0CEY7kfX87dwN6z6KS7',
#         'HOST': 'postgres://krishna:FvoIfuSMLEu7X0CEY7kfX87dwN6z6KS7@dpg-clg85deg1b2c73a66iq0-a.oregon-postgres.render.com/keralagram',  # Set to the hostname where your database is running, typically 'localhost'.
#         'PORT': '5432',  # Leave empty to use the default PostgreSQL port (5432).
#     }
# }

#local sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#local db.
# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'instagram',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',  # Set to the hostname where your database is running, typically 'localhost'.
#         'PORT': '5433',  # Leave empty to use the default PostgreSQL port (5432).
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# AUTH_USER_MODEL = 'users.Account'
LOGIN_URL = '/user/login/'
