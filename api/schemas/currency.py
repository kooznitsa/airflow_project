from sqlmodel import SQLModel, Field


class CurrencyBase(SQLModel):
    retrieved_at: str
    to_usd: float
    to_eur: float


class Currency(CurrencyBase, table=True):
    __tablename__ = 'currencies'
    id: int | None = Field(primary_key=True, default=None)


class CurrencyCreate(CurrencyBase):
    pass


class CurrencyRead(CurrencyBase):
    id: int
