import decimal
import pandas as pd
from datetime import date
from app.models import table_registry, Emissao

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