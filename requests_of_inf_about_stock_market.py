from functools import reduce

import finnhub
from finnhub import FinnhubAPIException

from functions_datetime import convert_string_date_to_datetime, convert_local_time_to_UTC, convert_UTC_to_local_time

# Setup client
api_key = 'my api key'
finnhub_client = finnhub.Client(api_key=api_key)


def get_stock_information(company):
    return finnhub_client.quote(company)


def get_current_value_of_stocks(company):
    current_value = get_stock_information(company)['c']
    return current_value


def count_current_value_of_all_stocks(dict_of_companies_and_stocks: dict):
    current_value_of_all_stocks = reduce(lambda x, y: x+y, dict_of_companies_and_stocks.values())
    return current_value_of_all_stocks


def get_set_of_stock_prices(start_date, finish_date, company, period):
    # Processing of dates in right format
    processed_start_date = convert_string_date_to_datetime(start_date)
    processed_finish_date = convert_string_date_to_datetime(finish_date)
    timestamp_1 = convert_local_time_to_UTC(processed_start_date)
    timestamp_2 = convert_local_time_to_UTC(processed_finish_date)
    try:
        set_of_data = finnhub_client.forex_candles(company, period, timestamp_1, timestamp_2)['c']
        set_of_date = finnhub_client.forex_candles(company, period, timestamp_1, timestamp_2)['t']
    except FinnhubAPIException:
        set_of_data = set_of_date = None
    return set_of_data, set_of_date
