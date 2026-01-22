import decimal
from datetime import date

from pydantic import BaseModel, ConfigDict


class EmissaoSchema(BaseModel):
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: str
    model_config = ConfigDict(from_attributes=True)

