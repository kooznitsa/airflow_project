from sqlalchemy import Column, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CurrencyCreate(Base):
    __abstract__ = True

    retrieved_at = Column(String)
    to_usd = Column(Float)
    to_eur = Column(Float)
