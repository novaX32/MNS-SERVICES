import resend
import traceback

from app.config import BUSINESS_EMAIL, RESEND_API_KEY

resend.api_key = RESEND_API_KEY


def send_email(to_email, subject, body):
    print("=" * 60)
    print("Sending email via Resend")
    print("TO:", to_email)

    try:
        response = resend.Emails.send({
            "from": "MNS Services <onboarding@resend.dev>",
            "to": to_email,
            "subject": subject,
            "text": body,
        })

        print("Email sent ✔")
        print("Response:", response)

    except Exception:
        print("EMAIL ERROR:")
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