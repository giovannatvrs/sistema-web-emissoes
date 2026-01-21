from sqlalchemy import registry, Mapped

table_registry = registry()

@table_registry.mapped_as_dataclass
class Emissao:
    __tablename__ = 'emissoes'
    id: Mapped[int]
    data: Mapped[date]
    tipo: Mapped[str]
    emissor: Mapped[str]
    valor: Mapped[decimal.Decimal]
    link: Mapped[str]