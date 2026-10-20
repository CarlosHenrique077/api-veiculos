from fastapi import HTTPException
from pymongo.errors import DuplicateKeyError

from app.models.veiculo import VeiculoIn
from app.repositories.veiculo_repository import VeiculoRepository
from app.utils.mongo import validar_id


class VeiculoService:
    def __init__(self):
        self.repo = VeiculoRepository()

    def _oid_ou_erro(self, id: str):
        oid = validar_id(id)
        if oid is None:
            raise HTTPException(status_code=400, detail="ID inválido")
        return oid

    def criar(self, veiculo: VeiculoIn) -> dict:
        try:
            return self.repo.inserir(veiculo.model_dump())
        except DuplicateKeyError:
            raise HTTPException(status_code=409, detail="Já existe veículo com essa placa")

    def listar(self) -> list[dict]:
        return self.repo.listar()

    def buscar(self, id: str) -> dict:
        veiculo = self.repo.buscar_por_id(self._oid_ou_erro(id))
        if veiculo is None:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")
        return veiculo

    def atualizar(self, id: str, veiculo: VeiculoIn) -> dict:
        oid = self._oid_ou_erro(id)
        try:
            atualizado = self.repo.atualizar(oid, veiculo.model_dump())
        except DuplicateKeyError:
            raise HTTPException(status_code=409, detail="Já existe veículo com essa placa")
        if atualizado is None:
            raise HTTPException(status_code=404, detail="Veículo não encontrado")
        return atualizado

    def excluir(self, id: str) -> None:
        if not self.repo.excluir(self._oid_ou_erro(id)):
            raise HTTPException(status_code=404, detail="Veículo não encontrado")