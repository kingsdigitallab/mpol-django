"""
Django settings for mpol project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

For production settings see
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
"""

import getpass
import logging
import os

import environ
from kdl_ldap.settings import *  # noqa

env = environ.Env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

PROJECT_NAME = "mpol"
PROJECT_TITLE = "Masonic Periodicals Online"

# -----------------------------------------------------------------------------
# Core Settings
# https://docs.djangoproject.com/en/dev/ref/settings/#id6
# -----------------------------------------------------------------------------

ADMINS = env.tuple("DJANGO_ADMINS", default=())
MANAGERS = ADMINS

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])

# https://docs.djangoproject.com/en/dev/ref/settings/#caches
# https://docs.djangoproject.com/en/dev/topics/cache/
# http://redis.io/topics/lru-cache
# http://niwibe.github.io/django-redis/
CACHE_REDIS_DATABASE = env.str("DJANGO_CACHE_REDIS_DATABASE", default="0")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/" + CACHE_REDIS_DATABASE,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "IGNORE_EXCEPTIONS": True,
        },
    }
}


CSRF_COOKIE_SECURE = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("POSTGRES_DB", default="app_mpol_liv"),
        "USER": env.str("POSTGRES_USER", default="app_mpol"),
        "PASSWORD": env.str("POSTGRES_PASSWORD", default=""),
        "HOST": env.str("POSTGRES_HOST", default="localhost"),
        "PORT": env.str("POSTGRES_PORT", default="5432"),
    }
}

# -----------------------------------------------------------------------------
# EMAIL SETTINGS
# -----------------------------------------------------------------------------

DEFAULT_FROM_EMAIL = env.str("DJANGO_DEFAULT_FROM_EMAIL", default="noreply@kcl.ac.uk")
EMAIL_HOST = env.str("DJANGO_EMAIL_HOST", default="smtp.kcl.ac.uk")
EMAIL_PORT = env.int("DJANGO_EMAIL_PORT", default=25)
EMAIL_HOST_USER = env.str("DJANGO_EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("DJANGO_EMAIL_HOST_PASSWORD", default="")
EMAIL_SUBJECT_PREFIX = "[Django {}] ".format(PROJECT_NAME)
EMAIL_USE_TLS = env.bool("DJANGO_EMAIL_USE_TLS", default=False)

# Sender of error messages to ADMINS and MANAGERS
SERVER_EMAIL = DEFAULT_FROM_EMAIL

INSTALLED_APPS = [
    "grappelli",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "compressor",
]

INSTALLED_APPS += [  # your project apps here
    "kdl_ldap",
    "rest_framework",
    "wagtail.wagtailcore",
    "wagtail.wagtailadmin",
    "wagtail.wagtaildocs",
    "wagtail.wagtailsnippets",
    "wagtail.wagtailusers",
    "wagtail.wagtailimages",
    "wagtail.wagtailembeds",
    "wagtail.wagtailredirects",
    "wagtail.wagtailforms",
    "wagtail.wagtailsites",
    "wagtail.contrib.wagtailapi",
    "wagtail.contrib.wagtailroutablepage",
    "wagtail.contrib.table_block",
    "taggit",
    "modelcluster",
    "haystack",
    "wagtail.wagtailsearch",
    "mpol",
    "cms",
    "periodicals",
]

INTERNAL_IPS = env.list("DJANGO_INTERNAL_IPS", default=["127.0.0.1"])

# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_L10N = False
USE_TZ = True

LOGGING_ROOT = os.path.join(BASE_DIR, "logs")
LOGGING_LEVEL = logging.WARN

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(levelname)s %(asctime)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            )
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.handlers.WatchedFileHandler",
            "filename": os.path.join(LOGGING_ROOT, "django.log"),
            "formatter": "verbose",
            "delay": True,
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file", "mail_admins"],
            "level": LOGGING_LEVEL,
            "propagate": True,
        },
        "mpol": {"handlers": ["file"], "level": LOGGING_LEVEL, "propagate": True},
        "periodicals": {
            "handlers": ["file"],
            "level": LOGGING_LEVEL,
            "propagate": True,
        },
    },
}

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.wagtailcore.middleware.SiteMiddleware",
    "wagtail.wagtailredirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = PROJECT_NAME + ".urls"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.messages.context_processors.messages",
                "mpol.context_processors.settings",
            ],
        },
    },
]

WSGI_APPLICATION = PROJECT_NAME + ".wsgi.application"

# -----------------------------------------------------------------------------
# Authentication
# https://docs.djangoproject.com/en/dev/ref/settings/#auth
# -----------------------------------------------------------------------------

if "wagtail.wagtailcore" in INSTALLED_APPS:
    LOGIN_URL = "/wagtail/login/"
else:
    LOGIN_URL = "/admin/login/"

# -----------------------------------------------------------------------------
# Sessions
# https://docs.djangoproject.com/en/dev/ref/settings/#sessions
# -----------------------------------------------------------------------------

SESSION_COOKIE_SECURE = True

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "SAMEORIGIN"

if env.bool("PRODUCTION", default=False):
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-proxy-ssl-header
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    # https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-secure
    SESSION_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-secure
    CSRF_COOKIE_SECURE = True
    # https://docs.djangoproject.com/en/dev/topics/security/#ssl-https
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-seconds
    SECURE_HSTS_SECONDS = 518400
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-preload
    SECURE_HSTS_PRELOAD = True
    # https://docs.djangoproject.com/en/dev/ref/middleware/#x-content-type-options-nosniff
    SECURE_CONTENT_TYPE_NOSNIFF = True

# -----------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# https://docs.djangoproject.com/en/dev/ref/settings/#static-files
# -----------------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, STATIC_URL.strip("/"))

if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

STATICFILES_DIRS = (os.path.join(BASE_DIR, "assets"),)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

MEDIA_URL = STATIC_URL + "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL.strip("/"))

if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

# -----------------------------------------------------------------------------
# Installed Applications Settings
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Django Compressor
# http://django-compressor.readthedocs.org/en/latest/
# -----------------------------------------------------------------------------

COMPRESS_ENABLED = True

COMPRESS_CSS_FILTERS = [
    # CSS minimizer
    "compressor.filters.cssmin.CSSMinFilter"
]

COMPRESS_PRECOMPILERS = (("text/x-scss", "django_libsass.SassCompiler"),)

# -----------------------------------------------------------------------------
# Django Grappelli
# http://django-grappelli.readthedocs.org/en/latest/
# -----------------------------------------------------------------------------

GRAPPELLI_ADMIN_TITLE = PROJECT_TITLE

# -----------------------------------------------------------------------------
# FABRIC
# -----------------------------------------------------------------------------

FABRIC_USER = getpass.getuser()

# -----------------------------------------------------------------------------
# GLOBALS FOR JS
# -----------------------------------------------------------------------------

# Google Analytics ID
GA_ID = "UA-67707155-2"

# -----------------------------------------------------------------------------
# Automatically generated settings
# -----------------------------------------------------------------------------

AUTH_LDAP_REQUIRE_GROUP = "cn=mpol," + LDAP_BASE_OU

ITEMS_PER_PAGE = env.int("DJANGO_ITEMS_PER_PAGE", default=10)

WAGTAIL_SITE_NAME = PROJECT_TITLE
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.wagtailsearch.backends.db",
    }
}

# Change as required
HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.solr_backend.SolrEngine",
        "URL": env.str("SOLR_URL", default="http://solr:8983/solr/default"),
        "TIMEOUT": 60 * 5,
        "INCLUDE_SPELLING": True,
        "BATCH_SIZE": 100,
    },
}
