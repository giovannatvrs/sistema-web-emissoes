import decimal
from datetime import date
from pydantic import BaseModel, ConfigDict
from typing import Optional

class EmissaoUpdate(BaseModel):
    data: Optional[date] = None
    tipo: Optional[str] = None
    emissor: Optional[str] = None
    valor: Optional[decimal.Decimal] = None
    link: Optional[str] = None

class EmissaoResponse(BaseModel):
    id: int
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: str
    model_config = ConfigDict(from_attributes=True)

class EmissaoPublic(BaseModel):
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: str
    model_config = ConfigDict(from_attributes=True)