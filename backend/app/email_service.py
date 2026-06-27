import resend
import traceback
from app.config import RESEND_API_KEY, FROM_EMAIL, BUSINESS_EMAIL

resend.api_key = RESEND_API_KEY


def send_email(to_email, subject, body):
    try:
        print("Sending email via Resend...")

        response = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": subject,
            "text": body,
        })

        print("Email response:", response)

        # IMPORTANT: check if email actually queued
        if response and "id" in response:
            print("Email successfully queued ✔")
        else:
            print("Warning: No email ID returned")

        return response

    except Exception as e:
        print("EMAIL ERROR OCCURRED ❌")
        traceback.print_exc()
        return None


def send_business_email(client):
    return send_email(
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
    return send_email(
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