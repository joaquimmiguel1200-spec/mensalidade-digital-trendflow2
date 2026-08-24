# Python 3.12+
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DECIMAL, ForeignKey
from .base import Base
from .enums import SubscriptionStatus, Frequency, PaymentMethod

class Plan(Base):
    __tablename__ = "plans"
    
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))
    price: Mapped[float] = mapped_column(DECIMAL(10, 2))
    frequency: Mapped[Frequency] = mapped_column(default=Frequency.MONTHLY)
    is_active: Mapped[bool] = mapped_column(default=True)

class Student(Base):
    __tablename__ = "students"
    
    full_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    document_id: Mapped[str] = mapped_column(String(20), unique=True) # CPF/CNPJ
    
    subscriptions: Mapped[list["Subscription"]] = relationship(back_populates="student")

class Subscription(Base):
    __tablename__ = "subscriptions"
    
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    status: Mapped[SubscriptionStatus] = mapped_column(default=SubscriptionStatus.PENDING)
    
    student: Mapped["Student"] = relationship(back_populates="subscriptions")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="subscription")

class Invoice(Base):
    __tablename__ = "invoices"
    
    subscription_id: Mapped[int] = mapped_column(ForeignKey("subscriptions.id"))
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2))
    due_date: Mapped[datetime]
    paid_at: Mapped[datetime | None]
    payment_method: Mapped[PaymentMethod | None]
    
    subscription: Mapped["Subscription"] = relationship(back_populates="invoices")