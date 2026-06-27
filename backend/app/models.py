from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    phone = Column(String(15), nullable=False)

    email = Column(String(150), nullable=False)

    service = Column(String(100), nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )