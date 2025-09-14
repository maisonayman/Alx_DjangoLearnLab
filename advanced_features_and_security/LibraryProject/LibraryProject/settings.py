
import os  # Make sure os is imported at the top
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vf4+(k@j&x#c+z9wx&q!9eb3ku(cu))*z4r!b+=epz)*4+xgy#'


# --- MODIFICATION 1: Set DEBUG to False in Production ---
# This is a best practice. Use an environment variable to control it.
DEBUG = True
# DEBUG = False # NEVER run with debug=True in production

ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['yourdomain.com'] # Set this for production

# --- MODIFICATION 2: Add Secure Settings for Production ---
# These settings should typically only be active when DEBUG is False.
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIFF = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True # Redirect all HTTP requests to HTTPS
    SECURE_HSTS_SECONDS = 31536000 # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


# Application definition

INSTALLED_APPS = [
    'relationship_app',
    'bookshelf',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'csp', # Add django-csp
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware', # Add CSP middleware early
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Configure your CSP rules. This is a basic "self only" policy.
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", 'https://fonts.googleapis.com') # Example: allowing Google Fonts
CSP_FONT_SRC = ("'self'", 'https://fonts.gstatic.com')

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "LibraryProject" / "static",
]

# ده اللي collectstatic هيجمع فيه كل الملفات
STATIC_ROOT = BASE_DIR / "staticfiles"



AUTH_USER_MODEL = "bookshelf.CustomUser"

# ===============================================================================
# SECURITY SETTINGS FOR PRODUCTION (Task 3)
# These settings should be active when DEBUG is False.
# ===============================================================================

# In a real production environment, DEBUG should be False.
# DEBUG = False
# ALLOWED_HOSTS = ['your.domain.com']

if 'PRODUCTION' in os.environ or not DEBUG:
    # This tells Django to trust the 'X-Forwarded-Proto' header from a proxy (like Nginx).
    # It's crucial for SECURE_SSL_REDIRECT to work correctly behind a reverse proxy.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    # --- Step 1: Configure Django for HTTPS Support ---
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

    # --- Step 2: Enforce Secure Cookies ---
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    # --- Step 3: Implement Secure Headers ---
    X_FRAME_OPTIONS = 'DENY'
    SECURE_CONTENT_TYPE_NOSNIF = True
    # The SECURE_BROWSER_XSS_FILTER is deprecated and no longer necessary in modern browsers.
    # A strong Content Security Policy (CSP), configured in Task 2, is the modern replacement.
    # We include it here for completeness as per the task requirements.
    SECURE_BROWSER_XSS_FILTER = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
