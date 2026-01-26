import decimal
from datetime import date
from pydantic import BaseModel, ConfigDict, ValidationError, field_validator, HttpUrl
from typing import Optional, List



class EmissaoUpdate(BaseModel):
    data: Optional[date] = None
    tipo: Optional[str] = None
    emissor: Optional[str] = None
    valor: Optional[decimal.Decimal] = None
    link: Optional[HttpUrl] = None

    @field_validator('data')
    def validate_data(cls, v):
        if v is not None and v > date.today():
            raise ValueError('Data invalida')
        return v

    @field_validator('tipo', 'emissor')
    def validate_tipo(cls, v):
        if not v.strip():
            raise ValueError('Campo não pode ser vazio')
        return v

    @field_validator('valor')
    def validate_valor(cls, v):
        if v < decimal.Decimal(0):
            raise ValueError('Valor invalido')
        return v





class EmissaoResponse(BaseModel):
    id: int
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: HttpUrl
    model_config = ConfigDict(from_attributes=True)

class EmissaoPublic(BaseModel):
    data: date
    tipo: str
    emissor: str
    valor: decimal.Decimal
    link: HttpUrl
    model_config = ConfigDict(from_attributes=True)

class EmissaoListResponse(BaseModel):
    emissoes: List[EmissaoResponse]
    total: int
