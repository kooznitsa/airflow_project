import asyncio
import logging

import aiohttp

from common.config.config import settings
from common.gateway.driver import GatewayAPIDriver
from common.schemas.currency import CurrencyCreate

logger = logging.getLogger(__name__)


class CurrencyParser:
    __BASE_URL = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/'
    foreign_currencies = ('eur', 'usd')
    target_currency = settings.TARGET_CURRENCY

    def _get_urls(self) -> list[str]:
        return [f'{self.__BASE_URL}{fc}.json' for fc in self.foreign_currencies]

    async def _fetch(self, session: aiohttp.ClientSession, url: str) -> dict:
        async with session.get(url) as response:
            if response.status != 200:
                response.raise_for_status()

            json_obj = await response.json()
            curr_date = json_obj.get('date')
            xchange_rate = json_obj.get('eur', json_obj.get('usd')).get(self.target_currency)

            return dict(zip(json_obj.keys(), (curr_date, xchange_rate)))

    async def _fetch_all(self, session: aiohttp.ClientSession) -> list:
        tasks = [asyncio.create_task(self._fetch(session, url)) for url in self._get_urls()]
        return await asyncio.gather(*tasks)

    async def _add_items_to_db(self, result: list) -> None:
        currency = CurrencyCreate(
            retrieved_at=result[0].get('date'),
            to_eur=result[0].get('eur'),
            to_usd=result[1].get('usd'),
        )
        await GatewayAPIDriver.create_currency(currency)

    async def get_currencies(self) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            result = await self._fetch_all(session)
            await self._add_items_to_db(result)

            logger.info(result)

            return result
