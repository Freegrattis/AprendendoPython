from typing import Optional

veiculos = []

class Veiculo:
    def __init__(self, id: int, marca: str, modelo: str, ano: int, placa: str):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def update(self, marca: Optional[str], modelo: Optional[str], ano: Optional[int], placa: Optional[str]):
        if marca is not None:
            self.marca = marca
        if modelo is not None:
            self.modelo = modelo
        if ano is not None:
            self.ano = ano
        if placa is not None:
            self.placa = placa

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "modelo": self.modelo,
            "ano": self.ano,
            "placa": self.placa,
        }
