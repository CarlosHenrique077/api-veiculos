from fastapi import APIRouter, Response, status

from app.models.veiculo import VeiculoIn, VeiculoOut
from app.services.veiculo_service import VeiculoService

router = APIRouter(prefix="/veiculos", tags=["Veículos"])
service = VeiculoService()


@router.post("", response_model=VeiculoOut, status_code=status.HTTP_201_CREATED)
def criar_veiculo(veiculo: VeiculoIn):
    return service.criar(veiculo)


@router.get("", response_model=list[VeiculoOut])
def listar_veiculos():
    return service.listar()


@router.get("/{id}", response_model=VeiculoOut)
def buscar_veiculo(id: str):
    return service.buscar(id)


@router.put("/{id}", response_model=VeiculoOut)
def atualizar_veiculo(id: str, veiculo: VeiculoIn):
    return service.atualizar(id, veiculo)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_veiculo(id: str):
    service.excluir(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)