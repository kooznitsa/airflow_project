from sqlalchemy import Column, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WeatherCreate(Base):
    __abstract__ = True

    retrieved_at = Column(String)
    temperature = Column(Float)
    wind_speed = Column(Float)
