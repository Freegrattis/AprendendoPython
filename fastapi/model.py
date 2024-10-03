from typing import Optional

from pydantic import BaseModel

class Futebol (BaseModel):
    id: Optional[int] = None
    nome_time: str 
    data_fundacao: str
    qtd_titulos: int
    estadio: str
