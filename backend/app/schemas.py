import decimal
from datetime import date

from pydantic import BaseModel


class EmissaoSchema(BaseModel):
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: str