# Python 3.12+
from pydantic import BaseModel, EmailStr, Field
from ..models.enums import Frequency, SubscriptionStatus

class PlanCreate(BaseModel):
    name: str = Field(..., min_length=3)
    price: float = Field(..., gt=0)
    frequency: Frequency
    description: str | None = None

class StudentEnrollment(BaseModel):
    full_name: str
    email: EmailStr
    document_id: str
    plan_id: int