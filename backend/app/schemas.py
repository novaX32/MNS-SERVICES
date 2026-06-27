from pydantic import BaseModel
from pydantic import EmailStr, Field


class ClientCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    phone: str = Field(min_length=10, max_length=15)
    email: EmailStr
    service: str = Field(min_length=3, max_length=100)


class ClientResponse(ClientCreate):
    id: int

    class Config:
        from_attributes = True