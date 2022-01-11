import asyncio
import json
import os

import aiohttp
from bs4 import BeautifulSoup

chart_500 = {}


async def get_exchange_rate(session, url):
    async with session.get(url) as response:
        response_text = await response.text()
        currency_soup = BeautifulSoup(response_text, "xml")
        exchange_rate = (
            currency_soup.find("Valute", ID="R01235")
            .find("Value")
            .text.strip()
            .replace(",", ".")
        )

        return round(float(exchange_rate), 2)


async def get_paginator(session, url):
    async with session.get(url) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, "lxml")

        footer_pages = soup.find("div", class_="finando_paging margin-top--small")
        pages = footer_pages.find_all("a")
        total_pages = 0
        for page in pages:
            current_page = int(page.text.strip()) if page.text.strip() != "" else 0
            total_pages = current_page if current_page > total_pages else total_pages

        return total_pages


async def usd_n_pages(url_usd, url_pages):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        tasks = [
            asyncio.create_task(get_exchange_rate(session, url_usd)),
            asyncio.create_task(get_paginator(session, url_pages)),
        ]
        responses = await asyncio.gather(*tasks)
    return responses


async def page_parcing(session, main_url, page):
    """Задача. Парсер, который пробегается по каждой странице и записывает данные."""
    url = f"{main_url}?p={page}"

    async with session.get(url) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, "lxml")

        table_lines = soup.find("table", class_="table__layout--fixed").find_all("tr")
        for line in table_lines:
            cell_first = line.find("td", class_="table__td--big")
            if not cell_first:
                continue

            title = cell_first.find("a").get("title")
            link = "https://markets.businessinsider.com" + cell_first.find("a").get(
                "href"
            )
            annual_growth = (
                line.find_all("td", class_="table__td")[7]
                .find_all("span")[1]
                .text.strip()
                .replace("%", "")
            )
            annual_growth_percent = round(float(annual_growth), 2)

            company_dict = {
                "link": link,
                "annual_growth_percent": annual_growth_percent,
            }
            chart_500[title] = company_dict


async def company_page_parcing(session, name, url, usd):
    async with session.get(url) as response:
        response_text = await response.text()

        company_soup = BeautifulSoup(response_text, "lxml")
        current_price = company_soup.find(
            "span", class_="price-section__current-value"
        ).text.strip()
        current_price = current_price.replace(",", "")
        current_price_rur = round(float(current_price) * float(usd), 2)
        company_code = (
            company_soup.find("span", class_="price-section__category")
            .text.strip()
            .replace("Stock , ", "")
        )
        data_items = company_soup.find_all("div", class_="snapshot__data-item")

        # there are two 'P/E Ratio' objects on the page
        for item in data_items:
            company_pe_ratio = None
            if "P/E Ratio" in item.find("div", class_="snapshot__header").contents[0]:
                company_pe_ratio = round(
                    float(item.contents[0].strip().replace(",", "")), 2
                )
                break

        week_low_class = company_soup.find(string="52 Week Low")
        if week_low_class:
            week_low_class = week_low_class.find_parent("div").find_parent("div")
            week_low_value = week_low_class.contents[0].strip().replace(",", "")
            week_high_class = (
                company_soup.find(string="52 Week High")
                .find_parent("div")
                .find_parent("div")
            )
            week_high_value = week_high_class.contents[0].strip().replace(",", "")
            relevant_profit = (
                round(float(week_high_value) / float(week_low_value), 2) * 100
            )
        else:
            relevant_profit = None

        result = {
            "code": company_code,
            "current_price_RUR": current_price_rur,
            "P/E_as_is": company_pe_ratio,
            "profit_percent": relevant_profit,
        }

        chart_500[name].update(result)


async def gather_data_from_site(url, total_pages):
    """Формировать необходимый список задач."""

    async with aiohttp.ClientSession(raise_for_status=True) as session:
        tasks = []

        for page in range(1, total_pages + 1):
            task = asyncio.create_task(page_parcing(session, url, page))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def gather_data_from_companies(usd):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        tasks = []

        for name, value in chart_500.items():
            url = value["link"]
            task = asyncio.create_task(company_page_parcing(session, name, url, usd))
            tasks.append(task)

        await asyncio.gather(*tasks)


def make_jsons():
    def none_vs_int(i, reverse=False):
        if i is None and not reverse:
            return float("inf")
        elif i is None and reverse:
            return float("-inf")
        return i

    # 1. Топ 10 компаний с самими дорогими акциями в рублях.
    with open(os.path.abspath("homework10/current_price_RUR.json"), "w") as file:
        sorted_dict = sorted(
            chart_500.items(),
            key=lambda x: none_vs_int(x[1]["current_price_RUR"], True),
            reverse=True,
        )
        sorted_dict = dict(sorted_dict[:10])
        json.dump(sorted_dict, file, indent=4, ensure_ascii=False)

    # 2. Топ 10 компаний с самым низким показателем P/E.
    with open(os.path.abspath("homework10/PE_as_is.json"), "w") as file:
        sorted_dict = sorted(
            chart_500.items(), key=lambda x: none_vs_int(x[1]["P/E_as_is"])
        )
        sorted_dict = dict(sorted_dict[:10])
        json.dump(sorted_dict, file, indent=4, ensure_ascii=False)

    # 3. Топ 10 компаний, которые показали самый высокий рост за последний год
    with open(os.path.abspath("homework10/annual_growth_percent.json"), "w") as file:
        sorted_dict = sorted(
            chart_500.items(),
            key=lambda x: none_vs_int(x[1]["annual_growth_percent"], True),
            reverse=True,
        )
        sorted_dict = dict(sorted_dict[:10])
        json.dump(sorted_dict, file, indent=4, ensure_ascii=False)

    # 4. Топ 10 комппаний, которые принесли бы наибольшую прибыль,
    # если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
    with open(os.path.abspath("homework10/profit_percent.json"), "w") as file:
        sorted_dict = sorted(
            chart_500.items(),
            key=lambda x: none_vs_int(x[1]["profit_percent"], True),
            reverse=True,
        )
        sorted_dict = dict(sorted_dict[:10])
        json.dump(sorted_dict, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main_url = "https://markets.businessinsider.com/index/components/s&p_500"
    usd_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    usd, total_pages = asyncio.run(usd_n_pages(usd_url, main_url))

    asyncio.run(gather_data_from_site(main_url, total_pages))
    asyncio.run(gather_data_from_companies(usd))

    make_jsons()
