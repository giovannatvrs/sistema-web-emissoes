from fastapi import FastAPI, HTTPException, status, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/emissoes")
def listar_emissoes():
    return

@app.get("/emissoes/{id}")
def listar_emissao(id: int):
    return

@app.put("/emissoes/{id}")
def editar_emissao(id: int):
    return

@app.get("/stats")
def dashboard():
    return