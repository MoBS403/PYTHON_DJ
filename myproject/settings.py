"""
Django settings for myproject project (Render-ready).
"""

from pathlib import Path
from decouple import AutoConfig
import os
import dj_database_url

# ======================================================
# BASE DIR
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent
config = AutoConfig(search_path=BASE_DIR)

# ======================================================
# SEGURANÇA
# ======================================================
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-1234567890abcdef1234567890abcdef"
)

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="localhost,127.0.0.1"
).split(",")

# Render (CSRF)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

# Proxy SSL (Render)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True

# ======================================================
# APLICAÇÕES
# ======================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "myapp",
]

# ======================================================
# MIDDLEWARE
# ======================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================================================
# URLS / WSGI / ASGI
# ======================================================
ROOT_URLCONF = "myproject.urls"
WSGI_APPLICATION = "myproject.wsgi.application"
ASGI_APPLICATION = "myproject.asgi.application"

# ======================================================
# TEMPLATES
# ======================================================
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

# ======================================================
# BANCO DE DADOS (PostgreSQL no Render, SQLite local)
# ======================================================
if os.getenv("DB_HOST"):
    # PostgreSQL remoto (Render/Aiven)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT", "5432"),
            "OPTIONS": {"sslmode": os.getenv("DB_SSLMODE", "require")},
        }
    }
else:
    # SQLite local
    DATABASES = {
        "default": dj_database_url.parse(
            os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
        )
    }

# ======================================================
# VALIDAÇÃO DE SENHAS
# ======================================================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ======================================================
# INTERNACIONALIZAÇÃO
# ======================================================
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ======================================================
# STATIC FILES (Render + WhiteNoise)
# ======================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ======================================================
# MEDIA FILES
# ======================================================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ======================================================
# PADRÕES
# ======================================================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ======================================================
# LOCALE
# ======================================================
LOCALE_PATHS = [BASE_DIR / "locale"]
