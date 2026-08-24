# Python 3.12+
from enum import StrEnum

class SubscriptionStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    PAST_DUE = "past_due"
    CANCELED = "canceled"
    INCOMPLETE = "incomplete"

class PaymentMethod(StrEnum):
    PIX = "pix"
    CREDIT_CARD = "credit_card"
    BOLETO = "boleto"
    RECURRING = "recurring"

class Frequency(StrEnum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"