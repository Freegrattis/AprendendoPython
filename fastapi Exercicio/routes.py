# routes.py

from fastapi import APIRouter, HTTPException
from models import Veiculo, veiculos
from utils import find_veiculo
from typing import Optional

router = APIRouter()

#criar um novo veículo
@router.post("/veiculos", response_model=dict)
def create_veiculo(marca: str, modelo: str, ano: int, placa: str):
    veiculo_id = len(veiculos) + 1
    novo_veiculo = Veiculo(id=veiculo_id, marca=marca, modelo=modelo, ano=ano, placa=placa)
    veiculos.append(novo_veiculo)
    return novo_veiculo.to_dict()

#ler um veículo por ID
@router.get("/veiculos/{veiculo_id}", response_model=dict)
def read_veiculo(veiculo_id: int):
    veiculo = find_veiculo(veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo.to_dict()

#atualizar parcialmente um veículo usando PATCH
@router.patch("/veiculos/{veiculo_id}", response_model=dict)
def update_veiculo(
    veiculo_id: int,
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    ano: Optional[int] = None,
    placa: Optional[str] = None
):
    veiculo = find_veiculo(veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    veiculo.update(marca, modelo, ano, placa)
    return veiculo.to_dict()

#deletar um veículo por ID
@router.delete("/veiculos/{veiculo_id}")
def delete_veiculo(veiculo_id: int):
    veiculo = find_veiculo(veiculo_id)
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    veiculos.remove(veiculo)
    return {"message": "Veículo deletado com sucesso"}
