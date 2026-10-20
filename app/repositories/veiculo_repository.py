from bson import ObjectId

from app.core.database import get_colecao
from app.utils.mongo import serializar


class VeiculoRepository:
    def __init__(self):
        self.colecao = get_colecao()

    def inserir(self, dados: dict) -> dict:
        resultado = self.colecao.insert_one(dados)
        return self.buscar_por_id(resultado.inserted_id)

    def listar(self) -> list[dict]:
        return [serializar(doc) for doc in self.colecao.find()]

    def buscar_por_id(self, oid: ObjectId) -> dict | None:
        doc = self.colecao.find_one({"_id": oid})
        return serializar(doc) if doc else None

    def atualizar(self, oid: ObjectId, dados: dict) -> dict | None:
        resultado = self.colecao.update_one({"_id": oid}, {"$set": dados})
        if resultado.matched_count == 0:
            return None
        return self.buscar_por_id(oid)

    def excluir(self, oid: ObjectId) -> bool:
        return self.colecao.delete_one({"_id": oid}).deleted_count > 0