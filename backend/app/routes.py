from fastapi import APIRouter, Depends, Request, BackgroundTasks
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Client
from app.schemas import ClientCreate

from app.email_service import send_business_email, send_customer_email
from app.core.rate_limiter import limiter

router = APIRouter(prefix="/api", tags=["Client Services"])


def send_emails_background(client: Client):
    print("🔥 EMAIL TASK TRIGGERED")
    print("📨 Background email started")

    try:
        send_business_email(client)
    except Exception as e:
        print("Business email failed:", e)

    try:
        send_customer_email(client)
    except Exception as e:
        print("Customer email failed:", e)


@router.post("/contact")
@limiter.limit("5/minute")
def submit_contact(
    request: Request,
    client: ClientCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    new_client = Client(
        name=client.name,
        phone=client.phone,
        email=client.email,
        service=client.service
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    background_tasks.add_task(send_emails_background, new_client)

    return {
        "success": True,
        "message": "Thanks for connecting. Email sent successfully."
    }