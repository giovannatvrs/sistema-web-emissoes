import decimal
import pandas as pd
from datetime import date
from sqlalchemy.orm import Session
from app.models import table_registry, Emissao
from app.database import engine
from pathlib import Path

table_registry.metadata.create_all(engine)


BASE_DIR = Path(__file__).resolve().parent.parent.parent
arquivo_excel = BASE_DIR / "data" / "Primario 2025.xlsx"

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