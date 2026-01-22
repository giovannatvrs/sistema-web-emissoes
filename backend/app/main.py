from fastapi import FastAPI, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Emissao
from app.schemas import EmissaoSchema
from typing import List

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/emissoes", response_model= List[EmissaoSchema])
def listar_emissoes(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    emissoes = db.query(Emissao).offset(skip).limit(limit).all()
    return  emissoes

@app.get("/emissoes/{id}")
def listar_emissao(id: int):
    return

@app.put("/emissoes/{id}")
def editar_emissao(id: int):
    return

@app.get("/stats")
def dashboard():
    return