import decimal
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from pathlib import Path
from datetime import date

from app.models import table_registry, Emissao

BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BACKEND_DIR / "data"

DATA_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_URL = f"sqlite:///{DATA_DIR}/emissoes.db"

engine = create_engine(DATABASE_URL, echo=True)
table_registry.metadata.create_all(engine)

arquivo_excel = './data/Primario 2025.xlsx'
df = pd.read_excel(arquivo_excel)

with Session(engine) as session:
    for index, row in df.iterrows():
        nova_emissao = Emissao(
            data=pd.to_datetime(row['Data']).date(),
            tipo=str(row['Tipo']),
            emissor=str(row['Emissor']),
            valor=decimal.Decimal(str(row['Valor'])),
            link=str(row['Link'])
        )
        session.add(nova_emissao)

    session.commit()