from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional

# Criação do app FastAPI
app = FastAPI()

# Configurações do banco de dados SQLite
DATABASE_URL = "sqlite:///./veiculos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modelo BD
class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String)
    ano = Column(Integer)
    placa = Column(String, unique=True)

# Cria as tabela
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/veiculos/", response_model=dict)
def create_veiculo(marca: str, modelo: str, ano: int, placa: str, db: Session = Depends(get_db)):
    veiculo = Veiculo(marca=marca, modelo=modelo, ano=ano, placa=placa)
    db.add(veiculo)
    db.commit()
    db.refresh(veiculo)
    return {"id": veiculo.id, "marca": veiculo.marca, "modelo": veiculo.modelo, "ano": veiculo.ano, "placa": veiculo.placa}

@app.get("/veiculos/{veiculo_id}", response_model=dict)
def read_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return {"id": veiculo.id, "marca": veiculo.marca, "modelo": veiculo.modelo, "ano": veiculo.ano, "placa": veiculo.placa}

@app.patch("/veiculos/{veiculo_id}", response_model=dict)
def update_veiculo(
    veiculo_id: int,
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    ano: Optional[int] = None,
    placa: Optional[str] = None,
    db: Session = Depends(get_db)
):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    if marca is not None:
        veiculo.marca = marca
    if modelo is not None:
        veiculo.modelo = modelo
    if ano is not None:
        veiculo.ano = ano
    if placa is not None:
        veiculo.placa = placa
    
    db.commit()
    db.refresh(veiculo)
    return {"id": veiculo.id, "marca": veiculo.marca, "modelo": veiculo.modelo, "ano": veiculo.ano, "placa": veiculo.placa}

@app.delete("/veiculos/{veiculo_id}")
def delete_veiculo(veiculo_id: int, db: Session = Depends(get_db)):
    veiculo = db.query(Veiculo).filter(Veiculo.id == veiculo_id).first()
    if veiculo is None:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    db.delete(veiculo)
    db.commit()
    return {"message": "Veículo deletado com sucesso"}

#Iniciar server automaticamente
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload= True)