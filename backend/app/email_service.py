import resend
import traceback
from app.config import RESEND_API_KEY, FROM_EMAIL, BUSINESS_EMAIL

resend.api_key = RESEND_API_KEY


def send_email(to_email, subject, body):
    try:
        print("=== EMAIL DEBUG START ===")
        print("FROM:", FROM_EMAIL)
        print("TO:", to_email)

        response = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": subject,
            "text": body,
        })

        print("RESEND RESPONSE:", response)
        print("=== EMAIL DEBUG END ===")

        return response

    except Exception as e:
        print("❌ EMAIL FULL ERROR:")
        import traceback
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