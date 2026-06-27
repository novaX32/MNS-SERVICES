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

    print("=" * 60)
    print("Starting email")
    print("SMTP_SERVER:", SMTP_SERVER)
    print("SMTP_PORT:", SMTP_PORT)
    print("FROM:", SMTP_EMAIL)
    print("TO:", to_email)

    try:
        print("Creating SMTP object...")

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
            timeout=30
        )

        print("Connected")

        server.set_debuglevel(1)

        print("EHLO")
        server.ehlo()

        print("STARTTLS")
        server.starttls()

        print("EHLO AGAIN")
        server.ehlo()

        print("LOGIN")
        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD
        )

        print("LOGIN SUCCESS")

        msg = MIMEMultipart()

        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        print("SENDING")

        server.sendmail(
            SMTP_EMAIL,
            to_email,
            msg.as_string()
        )

        print("EMAIL SENT")

        server.quit()

    except Exception:
        traceback.print_exc()


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