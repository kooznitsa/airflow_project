import logging

import aiohttp

from common.config.config import settings
from common.gateway.driver import GatewayAPIDriver
from common.schemas.weather import WeatherCreate

logger = logging.getLogger(__name__)


class WeatherParser:
    __URL = (
        f'https://api.open-meteo.com/v1/forecast?latitude={settings.LATITUDE}'
        f'&longitude={settings.LONGITUDE}'
        '&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,'
        'relative_humidity_2m,wind_speed_10m'
    )

    async def _add_items_to_db(self, result: dict) -> None:
        weather = WeatherCreate(
            retrieved_at=result.get('date'),
            temperature=result.get('temperature'),
            wind_speed=result.get('wind_speed'),
        )
        await GatewayAPIDriver.create_weather(weather)

    async def get_weather(self) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__URL) as response:
                json_obj = await response.json()
                current = json_obj.get('current')
                curr_date = current.get('time')
                temperature = current.get('temperature_2m')
                wind_speed = current.get('wind_speed_10m')

                result = {
                    'date': curr_date,
                    'temperature': temperature,
                    'wind_speed': wind_speed,
                }

                await self._add_items_to_db(result)

                logger.info(result)

                return result
