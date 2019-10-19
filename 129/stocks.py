import requests
from typing import Union, Tuple
from collections import Counter

STOCK_DATA = "https://bit.ly/2MzKAQg"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:


def _cap_str_to_mln_float(cap: str) -> Union[int, float]:
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0

    if "B" in cap:
        return float(cap.strip("$").strip("B")) * 1000

    return float(cap.strip("$").strip("M"))


def get_industry_cap(industry: str) -> float:
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    caps = [
        _cap_str_to_mln_float(entry["cap"])
        for entry in data
        if entry["industry"] == industry
    ]
    return round(sum(caps), 2)


def get_stock_symbol_with_highest_cap() -> str:
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    caps = [(entry["symbol"], _cap_str_to_mln_float(entry["cap"])) for entry in data]
    return max(caps, key=lambda x: x[1])[0]


def get_sectors_with_max_and_min_stocks() -> Tuple[str, str]:
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    stocks = [entry["sector"] for entry in data if entry["sector"] != "n/a"]
    stock_count = Counter(stocks).most_common()
    return stock_count[0][0], stock_count[-1][0]
