from fastapi import FastAPI, HTTPException, status, Depends
from model import Futebol
from typing import Optional, Any


app = FastAPI(title="API DTA JVL", version="1.0", description= "API Treinamento DTA")

# GET, POST, PUT e DELETE
# uvicorn main:app --reload

times = {
    1: {
        "nome_time": "Athletico Paranaense", 
        "data_fundacao": "21/03/1924",
        "qtd_titulos": 100,
        "estadio": "Ligga Arena"
    },
    2:{
        "nome_time": "Corinthians", 
        "data_fundacao": "01/09/1910",
        "qtd_titulos": 54,
        "estadio": "Neo Quimica Arena"
    },
}



@app.get("/")
async def raiz():
    return {"msg": "Deu certo"}

def fake_db():
    try:
        print("conectado")
    finally:
        print("desconectado")

@app.get("/times")
async def get_times(db: Any = Depends(fake_db)):
    return times

@app.get("/times/{time_id}")
async def get_time(time_id: int):
    try:
        time = times[time_id]
        return time
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Time não encontrado")

@app.post("/times", status_code=status.HTTP_201_CREATED)
async def post_time(time:Optional[Futebol] = None):
    next_id = len(times)+1
    times[next_id] = time
    del time.id
    return time

@app.put("/times/{time_id}")
async def put_time(time_id: int, time:Futebol):
    try:
        if time_id in times:
            times[time_id] = time
            time.id = time_id
            return time
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Time com id {time_id} nao encontrado") 
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error")

@app.delete("/times/{time_id}")
async def delete_time(time_id:int):
    try:
        if time_id in times:
            del times[time_id]
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Time com id {time_id} nao encontrado") 
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error")

#Iniciar server automaticamente
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload= True)