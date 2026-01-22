from fastapi import FastAPI, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session
from app.models import Emissao
from app.database import SessionLocal
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/emissoes")
def listar_emissoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    emissoes = db.query(Emissao).offset(skip).limit(limit).all()
    return  emissoes

@app.get("/emissoes/{id}")
def listar_emissao(id: int):
    return

@app.put("/emissoes/{id}")
def editar_emissao(id: int, emissao: Emissao):
    return

@app.get("/stats")
def dashboard():
    return