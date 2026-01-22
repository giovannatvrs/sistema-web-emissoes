from sqlalchemy.orm import registry, Mapped, mapped_column
from sqlalchemy import func
from datetime import date, datetime
import decimal


table_registry = registry()

@table_registry.mapped_as_dataclass
class Emissao:
    __tablename__ = 'emissoes'
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    data: Mapped[date]
    tipo: Mapped[str]
    emissor: Mapped[str]
    valor: Mapped[decimal.Decimal]
    link: Mapped[str]




