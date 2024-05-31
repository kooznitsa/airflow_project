from repositories.base import BaseRepository
from schemas.weather import Weather, WeatherCreate, WeatherRead


class WeatherRepository(BaseRepository):
    async def create(self, model: Weather, model_create: WeatherCreate) -> WeatherRead:
        return await super().create(Weather, model_create)

    async def get(self, model: Weather) -> WeatherRead:
        return await super().get(Weather)
