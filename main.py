# Python 3.12+
import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints import enrollment

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="2.0.0",
    description="TrendFlow 2 - Sistema White-Label de Gestão de Academias"
)

# Inclusão de Rotas
app.include_router(enrollment.router, prefix=f"{settings.API_V1_STR}/gym", tags=["Matrícula"])

@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "healthy", "version": "3.12"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)