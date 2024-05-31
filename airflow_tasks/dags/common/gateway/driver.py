import aiohttp

from common.config.config import settings
from common.schemas.currency import CurrencyCreate
from common.schemas.weather import WeatherCreate


class GatewayAPIDriver:
    _api_root_url: str = settings.GW_ROOT_URL

    class Route:
        currencies: str = 'currencies/'
        weather: str = 'weather/'

    @classmethod
    async def _build_url(cls, route: str) -> str:
        return f'{cls._api_root_url}{route}'

    @classmethod
    async def _post_data(
            cls,
            url: str,
            obj_create: CurrencyCreate | WeatherCreate,
    ) -> None:
        async with aiohttp.ClientSession() as session:
            await session.post(url, json=obj_create.__dict__)

    @classmethod
    async def create_currency(cls, model_create: CurrencyCreate) -> None:
        url = await cls._build_url(cls.Route.currencies)
        await cls._post_data(url, model_create)

    @classmethod
    async def create_weather(cls, model_create: WeatherCreate) -> None:
        url = await cls._build_url(cls.Route.weather)
        await cls._post_data(url, model_create)
