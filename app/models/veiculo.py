from typing import Optional

from pydantic import BaseModel, Field, field_validator


class VeiculoIn(BaseModel):
    marca: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    ano: int = Field(..., ge=1900, le=2100)
    placa: str = Field(..., min_length=7, max_length=8)
    cor: Optional[str] = None

    @field_validator("placa")
    @classmethod
    def placa_maiuscula(cls, v: str) -> str:
        return v.upper().strip()


class VeiculoOut(VeiculoIn):
    id: str