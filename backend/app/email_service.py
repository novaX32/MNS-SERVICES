import resend
import traceback
from app.config import RESEND_API_KEY, FROM_EMAIL, BUSINESS_EMAIL

resend.api_key = RESEND_API_KEY


def send_email(to_email, subject, html):
    try:
        print("Sending email via Resend...")

        response = resend.Emails.send({
            "from": FROM_EMAIL,
            "to": [to_email],
            "subject": subject,
            "html": html,   # ✅ HTML instead of text
        })

        print("Email response:", response)

        return response

    except Exception as e:
        print("EMAIL ERROR OCCURRED ❌")
        traceback.print_exc()
        return None


def send_business_email(client):
    html = f"""
    <h2>📩 New Lead Received</h2>
    <p><b>Name:</b> {client.name}</p>
    <p><b>Phone:</b> {client.phone}</p>
    <p><b>Email:</b> {client.email}</p>
    <p><b>Service:</b> {client.service}</p>
    """

    return send_email(
        BUSINESS_EMAIL,
        "New Service Request",
        html
    )


def send_customer_email(client):
    html = f"""
    <h2>Thanks for contacting MNS</h2>
    <p>Hi <b>{client.name}</b>,</p>

    <p>We received your request for <b>{client.service}</b>.</p>

    <p>Our team will contact you soon.</p>

    <br>
    <p>Regards,<br>MNS Team</p>
    """

    return send_email(
        client.email,
        "Thanks for contacting MNS",
        html
    )