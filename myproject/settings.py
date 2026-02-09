"""
Django settings for myproject
(Render + Aiven PostgreSQL)
"""

from pathlib import Path
import os
import dj_database_url

# ======================================================
# BASE DIR
# ======================================================
BASE_DIR = Path(__file__).resolve().parent.parent

# ======================================================
# SEGURANÇA
# ======================================================
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-fallback-key"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1"
).split(",")

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = False  # Render já força HTTPS

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

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
# BANCO DE DADOS (Render + Aiven)
# ======================================================
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
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
# STATIC FILES (WhiteNoise)
# ======================================================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

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
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# ======================================================
# EMAIL (DEV)
# ======================================================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
