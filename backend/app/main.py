from itertools import groupby

from fastapi import FastAPI, HTTPException, status, Path, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func, asc, desc, extract
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Emissao
from app.schemas import EmissaoResponse, EmissaoPublic, EmissaoUpdate, EmissaoListResponse
from typing import List, Optional
from datetime import date


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
def listar_emissoes(skip: int = 0,
                    limit: int = 30,
                    sort_by: str = "id",
                    order: str = "asc",
                    emissor: Optional[str] = None,
                    tipo: Optional[str] = None,
                    min_value: Optional[float] = None,
                    max_value: Optional[float] = None,
                    inicial_date: Optional[date] = None,
                    final_date: Optional[date] = None,
                    db: Session = Depends(get_db)):
    colunas = ["id", "data", "tipo", "emissor", "valor"];

    query = db.query(Emissao)

    if inicial_date is not None:
        query = query.filter(Emissao.data >= inicial_date)

    if final_date is not None:
        query = query.filter(Emissao.data <= final_date)

    if tipo:
        query = query.filter(Emissao.tipo.ilike(f"%{tipo}%"))

    if emissor:
        query = query.filter(Emissao.emissor.ilike(f"%{emissor}%"))

    if min_value is not None:
        query = query.filter(Emissao.valor >= min_value)

    if max_value is not None:
        query = query.filter(Emissao.valor <= max_value)


    if sort_by not in colunas:
        raise HTTPException(status_code=400, detail="Coluna inválida")

    coluna = getattr(Emissao, sort_by)
    ordem = asc if order == 'asc' else desc


    total_emissoes = query.count()

    emissoes = query.order_by(ordem(coluna)).offset(skip).limit(limit).all()


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
def get_estatisticas(db: Session = Depends(get_db)):
    volume_total = db.query(func.sum(Emissao.valor)).scalar()

    volume_total_por_ano = db.query(extract('year', Emissao.data).label("ano"),
                        func.sum(Emissao.valor).label("valor_total")).group_by("ano").order_by("ano").all()

    volume_total_por_ano_mes = db.query(extract('year', Emissao.data).label("ano"), extract('month', Emissao.data).label("mes"),
            func.sum(Emissao.valor).label("valor_total")).group_by("ano", "mes").order_by(  "ano", "mes").all()


    volume_por_tipo = db.query(Emissao.tipo, func.sum(Emissao.valor).label("valor_total")).group_by("tipo").order_by( "tipo").all()


    qtd_emissoes_ano = db.query(extract('year', Emissao.data).label("ano"), func.count(Emissao.id).label("qtd_emissoes")).group_by("ano").order_by("ano").all()

    qtd_emissoes_por_ano_mes = db.query(extract('year', Emissao.data).label("ano"), extract('month', Emissao.data).label("mes"),
        func.count(Emissao.id).label("qtd_emissoes")).group_by("ano", "mes").order_by("ano", "mes").all()


    qtd_emissoes_por_tipo = db.query(Emissao.tipo, func.count(Emissao.id).label("qtd_emissoes")).group_by("tipo").order_by("tipo").all()

    qtd_emissoes_por_emissor = db.query(Emissao.emissor, func.count(Emissao.id).label("qtd_emissoes")).group_by("emissor").order_by(func.count(Emissao.id).desc()).all()

    volume_medio = db.query(func.avg(Emissao.valor)).scalar()

    top_5_emissores_por_volume = db.query(Emissao.emissor, func.sum(Emissao.valor).label("valor_total")).group_by(
        Emissao.emissor).order_by(func.sum(Emissao.valor).desc()).limit(5).all()
    top_5_emissores_por_qtd = db.query(Emissao.emissor, func.count(Emissao.id).label("qtd_emissoes")).group_by(
        Emissao.emissor).order_by(func.count(Emissao.id).desc()).limit(5).all()
    tipos_mais_relevantes_por_volume = db.query(Emissao.tipo, func.sum(Emissao.valor).label("valor_total")).group_by(
        Emissao.tipo).order_by(func.sum(Emissao.valor).desc()).all()


    return {
        "volume_total": volume_total,
        "volume_medio": volume_medio,
        "volume_por_ano": [{"ano": r.ano, "valor_total": r.valor_total} for r in volume_total_por_ano],
        "volume_por_ano_mes": [{"ano": r.ano, "mes": r.mes, "valor_total": r.valor_total}
                               for r in volume_total_por_ano_mes],
        "volume_por_tipo": [{"tipo": r.tipo, "valor_total": r.valor_total}
                               for r in volume_por_tipo],
        "qtd_emissoes_por_ano": [{"ano": r.ano, "qtd_emissoes": r.qtd_emissoes}
                                for r in qtd_emissoes_ano],
        "qtd_emissoes_por_ano_mes": [{"ano": r.ano, "mes": r.mes, "qtd_emissoes": r.qtd_emissoes}
                                     for r in qtd_emissoes_por_ano_mes],
        "qtd_emissoes_por_tipo": [{"tipo": r.tipo, "qtd_emissoes": r.qtd_emissoes}
                                for r in qtd_emissoes_por_tipo],
        "maiores_emissores_por_volume": [{"emissor": r.emissor, "valor_total": r.valor_total} for r in
                                       top_5_emissores_por_volume],
        "maiores_emissores_por_qtd": [{"emissor": r.emissor, "qtd_emissoes": r.qtd_emissoes} for r in
                                    top_5_emissores_por_qtd],
        "tipos_mais_relevantes_por_volume": [{"tipo": r.tipo, "valor_total": r.valor_total} for r in
                                             tipos_mais_relevantes_por_volume]
    }