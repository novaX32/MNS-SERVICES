from dotenv import load_dotenv
import os

load_dotenv()


def must_get(key):
    value = os.getenv(key)
    if not value:
        raise Exception(f"Missing environment variable: {key}")
    return value


DATABASE_URL = must_get("DATABASE_URL")

RESEND_API_KEY = must_get("RESEND_API_KEY")
FROM_EMAIL = must_get("FROM_EMAIL")

BUSINESS_EMAIL = must_get("BUSINESS_EMAIL")