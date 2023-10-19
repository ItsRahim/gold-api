"""
This is a Python file used to store information websites.

It provides a centralised location for all sources this api will use to gather information about gold prices.
Information includes website name, url and html elements to scrape

Author: Rahim Ahmed
Version: 1.0
"""

"""
Data Source: Investing.com

This script scrapes data from the Investing.com website to retrieve
current XAU/GBP price information.
"""
UK_INVESTING_DICT = {
    "name": "UK Investing",
    "url": "https://uk.investing.com/currencies/xau-gbp",
    "element": ["span", {"class": "text-2xl", "data-test": "instrument-price-last"}]
}

# TODO: Change implementation - DO NOT USE
_TRADING_VIEW_DICT = {
    "name": "Trading View",
    "url": "https://www.tradingview.com/symbols/XAUGBP/",
    "element": ["span", {"class": "last-JWoJqCpY js-symbol-last"}]
}


# TODO: Fix the element to retrieve price - DO NOT USE
_BLOOMBERG_DICT = {
    "name": "Bloomberg",
    "url": "https://www.bloomberg.com/quote/XAUGBP:CUR",
    "element": ["div", {'data-component': 'sized-price', 'class': 'sized-price SizedPrice_extraLarge-05pKbJRbUH8-'}]
}


CNBC_DICT = {
    "name": "CNBC",
    "url": "https://www.cnbc.com/quotes/XAUGBP=",
    "element": ["span", {'class': 'QuoteStrip-lastPrice'}]
}


FORBES_DICT = {
    "name": "Forbes",
    "url": "https://www.forbes.com/advisor/money-transfer/currency-converter/xau-gbp/",
    "element": ["span", {'class': 'amount'}]
}


# TODO: Fake user agent required
GOLD_UK_DICT = {
        "name": "Gold UK",
        "url": "https://www.cnbc.com/quotes/XAUGBP=",
        "element": ["span", {'class': 'QuoteStrip-lastPrice'}]
}


# TODO: Fake user agent required
BULLION_BY_POST_DICT = {
    "name": "BullionByPost",
    "url": "https://www.bullionbypost.co.uk/gold-price/",
    "element": ["span", {'name': 'current_price_field', 'data-currency': 'default'}]
}

