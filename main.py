import os
from typing import Optional

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field, field_validator
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["garagem"]
colecao = db["veiculos"]

app = FastAPI(title="API de Veículos")


class VeiculoIn(BaseModel):
    marca: str = Field(..., min_length=1)
    modelo: str = Field(..., min_length=1)
    ano: int = Field(..., ge=1900, le=2100)
    placa: str = Field(..., min_length=7, max_length=8)
    cor: Optional[str] = None

    @field_validator("placa")
    @classmethod
    def placa_maiuscula(cls, v):
        return v.upper().strip()


def validar_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except (InvalidId, TypeError):
        raise HTTPException(status_code=400, detail="ID inválido")


def serializar(doc: dict) -> dict:
    doc["id"] = str(doc.pop("_id"))
    return doc


@app.post("/veiculos", status_code=status.HTTP_201_CREATED)
def criar_veiculo(veiculo: VeiculoIn):
    if colecao.find_one({"placa": veiculo.placa}):
        raise HTTPException(status_code=409, detail="Já existe veículo com essa placa")
    resultado = colecao.insert_one(veiculo.model_dump())
    return serializar(colecao.find_one({"_id": resultado.inserted_id}))


@app.get("/veiculos")
def listar_veiculos():
    return [serializar(doc) for doc in colecao.find()]


@app.get("/veiculos/{id}")
def buscar_veiculo(id: str):
    doc = colecao.find_one({"_id": validar_id(id)})
    if doc is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return serializar(doc)


@app.put("/veiculos/{id}")
def atualizar_veiculo(id: str, veiculo: VeiculoIn):
    oid = validar_id(id)
    if colecao.find_one({"placa": veiculo.placa, "_id": {"$ne": oid}}):
        raise HTTPException(status_code=409, detail="Já existe veículo com essa placa")
    resultado = colecao.update_one({"_id": oid}, {"$set": veiculo.model_dump()})
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return serializar(colecao.find_one({"_id": oid}))


@app.delete("/veiculos/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_veiculo(id: str):
    resultado = colecao.delete_one({"_id": validar_id(id)})
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
