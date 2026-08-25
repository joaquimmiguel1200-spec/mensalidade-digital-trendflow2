"""
Exceções customizadas da aplicação
"""
from fastapi import HTTPException, status


class APIException(HTTPException):
    """Exceção base para a API"""
    pass


class UnauthorizedException(APIException):
    """Não autorizado"""
    def __init__(self, detail: str = "Não autorizado"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
        )


class ForbiddenException(APIException):
    """Acesso proibido"""
    def __init__(self, detail: str = "Acesso proibido"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )


class NotFoundException(APIException):
    """Recurso não encontrado"""
    def __init__(self, detail: str = "Recurso não encontrado"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
        )


class ValidationException(APIException):
    """Erro de validação"""
    def __init__(self, detail: str = "Erro de validação"):
        super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=detail,
        )


class ConflictException(APIException):
    """Conflito de dados"""
    def __init__(self, detail: str = "Conflito de dados"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
        )


class PaymentException(APIException):
    """Erro de pagamento"""
    def __init__(self, detail: str = "Erro ao processar pagamento"):
        super().__init__(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail=detail,
        )


class CrossTenantAccessException(APIException):
    """Tentativa de acesso entre academias"""
    def __init__(self, detail: str = "Acesso negado: dados de outra academia"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
        )
