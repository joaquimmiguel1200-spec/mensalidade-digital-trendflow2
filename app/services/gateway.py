# Python 3.12+
import logging
from abc import ABC, abstractmethod
from ..models.enums import PaymentMethod

logger = logging.getLogger(__name__)

class PaymentGateway(ABC):
    """Interface abstrata para Gateways de Pagamento (Pagar.me, Stripe, etc)"""
    
    @abstractmethod
    async def process_recurring(self, amount: float, customer_data: dict) -> bool:
        pass

    @abstractmethod
    async def generate_pix(self, amount: float) -> str:
        pass

class MockGateway(PaymentGateway):
    """Implementação Mock para o TrendFlow 2"""
    
    async def process_recurring(self, amount: float, customer_data: dict) -> bool:
        logger.info(f"Simulando cobrança recorrente de R${amount} para {customer_data.get('email')}")
        return True # Simula sucesso

    async def generate_pix(self, amount: float) -> str:
        return "00020126360014BR.GOV.BCB.PIX0114+5511999999999"