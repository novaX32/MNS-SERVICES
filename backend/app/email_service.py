import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import traceback
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import (
    SMTP_SERVER,
    SMTP_PORT,
    SMTP_EMAIL,
    SMTP_PASSWORD,
    BUSINESS_EMAIL
)


def send_email(to_email, subject, body):
    print("=" * 50)

    try:
        socket.setdefaulttimeout(10)

        print("Connecting...")

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587,
            timeout=10
        )

        print("Connected")

        server.ehlo()
        print("EHLO OK")

        server.starttls()
        print("TLS OK")

        server.login(
            "chavannikhil762@gmail.com",
            "YOUR_16_CHARACTER_APP_PASSWORD"
        )

        print("LOGIN OK")

        server.quit()

    except Exception as e:
        print("FULL ERROR:", repr(e))


def send_business_email(client):
    send_email(
        BUSINESS_EMAIL,
        "New Service Request",
        f"""
Name: {client.name}
Phone: {client.phone}
Email: {client.email}
Service: {client.service}
"""
    )


def send_customer_email(client):
    send_email(
        client.email,
        "Thanks for contacting MNS",
        f"""
Hi {client.name},

We received your request.

We will contact you soon.

Regards,
MNS Team
"""
    )