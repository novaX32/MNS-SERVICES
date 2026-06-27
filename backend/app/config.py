from dotenv import load_dotenv
import os

load_dotenv()

def must_get(key):
    value = os.getenv(key)
    if not value:
        raise Exception(f"Missing environment variable: {key}")
    return value


DATABASE_URL = must_get("DATABASE_URL")

SMTP_SERVER = must_get("SMTP_SERVER")   # 🔥 FIXED
SMTP_PORT = int(must_get("SMTP_PORT"))   # 🔥 FIXED

SMTP_EMAIL = must_get("SMTP_EMAIL")
SMTP_PASSWORD = must_get("SMTP_PASSWORD")

BUSINESS_EMAIL = must_get("BUSINESS_EMAIL")