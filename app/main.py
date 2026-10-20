from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import configurar_banco
from app.routes import veiculos


@asynccontextmanager
async def lifespan(app: FastAPI):
    configurar_banco()
    yield


app = FastAPI(
    title="API de Veículos",
    description="CRUD de veículos com FastAPI e MongoDB",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(veiculos.router)