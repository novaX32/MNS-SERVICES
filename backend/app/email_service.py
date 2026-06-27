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

    print("Sending email...")

    try:
        # 🔥 CREATE NEW CONNECTION EVERY TIME (VERY IMPORTANT)
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)

        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(SMTP_EMAIL, SMTP_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(
            SMTP_EMAIL,
            to_email,
            msg.as_string()
        )

        server.quit()

        print("Email sent ✔")

    except Exception as e:
        print("Email Error:", e)


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