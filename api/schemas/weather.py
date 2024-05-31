from sqlmodel import SQLModel, Field


class WeatherBase(SQLModel):
    retrieved_at: str
    temperature: float
    wind_speed: float


class Weather(WeatherBase, table=True):
    __tablename__ = 'weather'
    id: int | None = Field(primary_key=True, default=None)


class WeatherCreate(WeatherBase):
    pass


class WeatherRead(WeatherBase):
    id: int
