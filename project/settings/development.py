from project.settings.base import *

# # ----------------------------------------------------
# # *** Allowed Hosts ***
# # ----------------------------------------------------
ALLOWED_HOSTS = ["*"]


# KNOX Configuration
KNOX_TOKEN_MODEL = "knox.AuthToken"

REST_KNOX = {
    # "SECURE_HASH_ALGORITHM": "hashlib.sha512",
    "AUTH_TOKEN_CHARACTER_LENGTH": 64,
    # "TOKEN_TTL": timedelta(hours=730),
    "TOKEN_TTL": None,  # Never Expire
    "USER_SERIALIZER": "knox.serializers.UserSerializer",
    "TOKEN_LIMIT_PER_USER": None,
    "AUTO_REFRESH": False,
    "MIN_REFRESH_INTERVAL": 60,
    "AUTH_HEADER_PREFIX": "Token",
    "EXPIRY_DATETIME_FORMAT": api_settings.DATETIME_FORMAT,
    "TOKEN_MODEL": "knox.AuthToken",
}

# Swagger Configuration
SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    },
    "JSON_EDITOR": True,
}

# Mail Config
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = config.EMAIL_PORT
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = config.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER