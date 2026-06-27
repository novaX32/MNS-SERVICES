from app.email_service import send_business_email
from types import SimpleNamespace

client = SimpleNamespace(
    name="Test User",
    phone="9999999999",
    email="your-email@gmail.com",
    service="Testing"
)

send_business_email(client)