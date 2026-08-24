# Python 3.12+
from fastapi import APIRouter, HTTPException, status
from ...schemas.subscription import StudentEnrollment
from ...services.gateway import MockGateway

router = APIRouter()
gateway = MockGateway()

@router.post("/enroll", status_code=status.HTTP_201_CREATED)
async def create_digital_enrollment(enrollment: StudentEnrollment):
    """
    Fluxo de Matrícula Digital:
    1. Valida dados
    2. Cria registro do aluno
    3. Inicia processamento de pagamento
    4. Ativa matrícula (após confirmação)
    """
    # Lógica de persistência no DB aqui (omitida para brevidade)
    
    payment_success = await gateway.process_recurring(
        amount=199.90, # Exemplo vindo do plano
        customer_data={"email": enrollment.email}
    )
    
    if not payment_success:
        raise HTTPException(status_code=400, detail="Falha no processamento do pagamento")
        
    return {
        "message": "Matrícula realizada com sucesso",
        "status": "active",
        "student": enrollment.full_name
    }