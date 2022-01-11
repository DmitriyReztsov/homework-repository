import asyncio
from unittest import mock

import aiohttp
import pytest

from homework10 import async_hw10


@pytest.mark.asyncio
async def test_get_currency_exchange():
    usd_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(async_hw10.get_exchange_rate(session, usd_url)),
        ]
        response = await asyncio.gather(*tasks)
    assert isinstance(response[0], float)
