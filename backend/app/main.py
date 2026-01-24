from fastapi import FastAPI, HTTPException, status, Path, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, asc, desc
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Emissao
from app.schemas import EmissaoResponse, EmissaoPublic, EmissaoUpdate, EmissaoListResponse
from typing import List


app = FastAPI()

origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/emissoes", response_model= EmissaoListResponse)
def listar_emissoes(skip: int = 0, limit: int = 30, sort_by: str | None = None, order: str = "asc", db: Session = Depends(get_db)):
    colunas = ["id", "data", "tipo", "emissor", "valor"];

    if sort_by not in colunas:
        raise HTTPException(status_code=400, detail="Coluna inválida")

    coluna = getattr(Emissao, sort_by)
    ordem = asc if order == 'asc' else 'desc'



    emissoes = db.query(Emissao).order_by(ordem(coluna)).offset(skip).limit(limit).all()

    total_emissoes = db.query(func.count(Emissao.id)).scalar()

    return  {
        "emissoes": emissoes,
        "total": total_emissoes,
    }

@app.get("/emissoes/{id}", response_model= EmissaoListResponse)
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