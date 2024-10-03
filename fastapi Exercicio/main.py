# main.py

from fastapi import FastAPI
from routes import router

app = FastAPI()

# Inclui as rotas definidas em routes.py
app.include_router(router)

 #Iniciar server automaticamente
if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="info", reload= True)