import decimal
import pandas as pd
import os
from datetime import date
from sqlalchemy.orm import Session
from app.models import table_registry, Emissao
from app.database import engine
from pathlib import Path

table_registry.metadata.create_all(engine)

BASE_DIR = Path(__file__).resolve().parent
arquivo_excel = BASE_DIR.parent.parent / "data" / "Primario 2025.xlsx"

if arquivo_excel.exists():
    df = pd.read_excel(arquivo_excel)

    with Session(engine) as session:
        session.query(Emissao).delete()
        session.commit()
        for index, row in df.iterrows():
            valor_raw = str(row['Valor']).replace(',', '.') if pd.notnull(row['Valor']) else "0"

            nova_emissao = Emissao(
                data=pd.to_datetime(row['Data']).date(),
                tipo=str(row['Tipo']),
                emissor=str(row['Emissor']),
                valor=decimal.Decimal(valor_raw),
                link=str(row['Link']) if pd.notnull(row['Link']) else ""
            )
            session.add(nova_emissao)

        session.commit()