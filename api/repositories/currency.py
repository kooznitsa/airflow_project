from repositories.base import BaseRepository
from schemas.currency import Currency, CurrencyCreate, CurrencyRead


class CurrencyRepository(BaseRepository):
    async def create(self, model: Currency, model_create: CurrencyCreate) -> CurrencyRead:
        return await super().create(Currency, model_create)

    async def get(self, model: Currency) -> CurrencyRead:
        return await super().get(Currency)
