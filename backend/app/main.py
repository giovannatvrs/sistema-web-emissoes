from fastapi import FastAPI, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Emissao
from app.schemas import EmissaoResponse, EmissaoPublic, EmissaoUpdate
from typing import List


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/emissoes", response_model= List[EmissaoResponse])
def listar_emissoes(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    emissoes = db.query(Emissao).offset(skip).limit(limit).all()
    return  emissoes

@app.get("/emissoes/{id}", response_model= EmissaoResponse)
def obter_emissao(id: int, db: Session = Depends(get_db)):
    emissao = db.query(Emissao).filter(Emissao.id == id).first()
    if not emissao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = 'Emissão não encontrada'
        )
    return emissao

@app.put("/emissoes/{id}", response_model= EmissaoResponse)
def editar_emissao(id: int, emissao: EmissaoUpdate, db: Session = Depends(get_db)):
    db_emissao = db.query(Emissao).filter(Emissao.id == id).first()
    if not db_emissao:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail = 'Emissão não encontrada'
        )
    dados_atualizados = emissao.model_dump(exclude_unset=True)
    for k, v in dados_atualizados.items():
        setattr(db_emissao, k, v)

    db.commit()
    db.refresh(db_emissao)

    return db_emissao

@app.get("/stats")
def dashboard():
    return