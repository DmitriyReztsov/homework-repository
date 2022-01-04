from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-*k_u8+-_z(l!bznp5_&+*&%!ut&*x(k58at-l@xfcz!p!vj*_#"

INSTALLED_APPS = [
    "humans",
    "homeworks",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "main.db",
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False
