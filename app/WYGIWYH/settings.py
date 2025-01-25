"""
Django settings for WYGIWYH project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
import sys
from pathlib import Path


SITE_TITLE = "WYGIWYH"
TITLE_SEPARATOR = "::"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1").split(" ")
CSRF_TRUSTED_ORIGINS = os.environ.get("URL", "http://localhost http://127.0.0.1").split(
    " "
)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "webpack_boilerplate",
    "django.contrib.humanize",
    "django.contrib.postgres",
    "django_browser_reload",
    "django.forms",
    "debug_toolbar",
    "crispy_forms",
    "crispy_bootstrap5",
    "hijack",
    "hijack.contrib.admin",
    "django_filters",
    "apps.users.apps.UsersConfig",
    "procrastinate.contrib.django",
    "apps.transactions.apps.TransactionsConfig",
    "apps.currencies.apps.CurrenciesConfig",
    "apps.accounts.apps.AccountsConfig",
    "apps.common.apps.CommonConfig",
    "apps.net_worth.apps.NetWorthConfig",
    "apps.import_app.apps.ImportConfig",
    "apps.api.apps.ApiConfig",
    "cachalot",
    "rest_framework",
    "drf_spectacular",
    "django_cotton",
    "apps.rules.apps.RulesConfig",
    "apps.calendar_view.apps.CalendarViewConfig",
    "apps.dca.apps.DcaConfig",
    "pwa",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "apps.common.middleware.localization.LocalizationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "hijack.middleware.HijackUserMiddleware",
]

ROOT_URLCONF = "WYGIWYH.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

WHITENOISE_MANIFEST_STRICT = False

WSGI_APPLICATION = "WYGIWYH.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "users.User"


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", "English"),
    ("nl", "Nederlands"),
    ("pt-br", "Português (Brasil)"),
)

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static_files"

STATICFILES_DIRS = [
    ROOT_DIR / "frontend/build",
    BASE_DIR / "static",
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}

WEBPACK_LOADER = {
    "MANIFEST_FILE": ROOT_DIR / "frontend/build/manifest.json",
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login/"

# CRISPY FORMS
CRISPY_ALLOWED_TEMPLATE_PACKS = ["bootstrap5", "crispy_forms/pure_text"]
CRISPY_TEMPLATE_PACK = "bootstrap5"

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = int(os.getenv("SESSION_EXPIRY_TIME", 2678400))  # 31 days
SESSION_COOKIE_SECURE = os.getenv("HTTPS_ENABLED", "false").lower() == "true"

DEBUG_TOOLBAR_CONFIG = {
    "ROOT_TAG_EXTRA_ATTRS": "hx-preserve",
    "SHOW_TOOLBAR_CALLBACK": lambda r: False,  # disables it}
}
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
    "cachalot.panels.CachalotPanel",
]
INTERNAL_IPS = [
    "127.0.0.1",
]

if DEBUG:
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
    try:
        _, _, ips = socket.gethostbyname_ex("node")
        INTERNAL_IPS.extend(ips)
    except socket.gaierror:
        # The node container isn't started (yet?)
        pass


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.DjangoModelPermissions"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "WYGIWYH API",
    "DESCRIPTION": "A no-frills expense tracker",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

if "procrastinate" in sys.argv:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "procrastinate": {
                "format": "%(asctime)s %(levelname)-7s %(name)s %(message)s"
            },
        },
        "handlers": {
            "procrastinate": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "procrastinate",
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "procrastinate": {
                "handlers": ["procrastinate"],
                "level": "INFO",
                "propagate": False,
            },
            "root": {
                "handlers": ["console"],
                "level": "INFO",
            },
        },
    }
else:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "procrastinate": {
                "format": "%(asctime)s %(levelname)-7s %(name)s %(message)s"
            },
        },
        "handlers": {
            "procrastinate": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "procrastinate",
            },
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "loggers": {
            "procrastinate": {
                "handlers": None,
                "level": "INFO",
                "propagate": False,
            },
            "root": {
                "handlers": ["console"],
                "level": "INFO",
            },
        },
    }

CACHALOT_UNCACHABLE_TABLES = ("django_migrations", "procrastinate_jobs")


# PWA
PWA_APP_NAME = SITE_TITLE
PWA_APP_DESCRIPTION = "A simple and powerful finance tracker"
PWA_APP_THEME_COLOR = "#fbb700"
PWA_APP_BACKGROUND_COLOR = "#222222"
PWA_APP_DISPLAY = "standalone"
PWA_APP_SCOPE = "/"
PWA_APP_ORIENTATION = "any"
PWA_APP_START_URL = "/"
PWA_APP_STATUS_BAR_COLOR = "default"
PWA_APP_ICONS = [
    {"src": "/static/img/favicon/android-icon-192x192.png", "sizes": "192x192"}
]
PWA_APP_ICONS_APPLE = [
    {"src": "/static/img/favicon/apple-icon-180x180.png", "sizes": "180x180"}
]
PWA_APP_SPLASH_SCREEN = [
    {
        "src": "/static/img/pwa/splash-640x1136.png",
        "media": "(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)",
    }
]
PWA_APP_DIR = "ltr"
PWA_APP_LANG = "en-US"
PWA_APP_SHORTCUTS = [
    {
        "name": "New Transaction",
        "url": "/add/",
        "description": "Add new transaction",
    }
]
PWA_APP_SCREENSHOTS = [
    {
        "src": "/static/img/pwa/splash-750x1334.png",
        "sizes": "750x1334",
        "type": "image/png",
        "form_factor": "wide",
    },
    {
        "src": "/static/img/pwa/splash-750x1334.png",
        "sizes": "750x1334",
        "type": "image/png",
    },
]
PWA_SERVICE_WORKER_PATH = BASE_DIR / "templates" / "pwa" / "serviceworker.js"

ENABLE_SOFT_DELETE = os.getenv("ENABLE_SOFT_DELETE", "false").lower() == "true"
KEEP_DELETED_TRANSACTIONS_FOR = int(os.getenv("KEEP_DELETED_ENTRIES_FOR", "365"))
