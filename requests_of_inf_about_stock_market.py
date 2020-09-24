from functools import reduce

import finnhub
from finnhub import FinnhubAPIException

from functions_datetime import convert_string_date_to_datetime, convert_local_time_to_UTC, convert_UTC_to_local_time

# Setup client
finnhub_client = finnhub.Client(api_key="bsjtdf7rh5rdj1numnqg")


def get_stock_information(company):
    return finnhub_client.quote(company)


def get_current_value_of_stocks(company):
    current_value = get_stock_information(company)['c']
    return current_value


def count_current_value_of_all_stocks(dict_of_companies_and_stocks: dict):
    current_value_of_all_stocks = reduce(lambda x, y: x+y, dict_of_companies_and_stocks.values())
    return current_value_of_all_stocks


# 2020-07-08
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


# print(get_set_of_stock_prices('2020-08-20', '2020-08-27', 'AAPL', 'D'))
# aapl_time = get_set_of_stock_prices('2020-07-28', '2020-08-16', 'AAPL', 'D')
# # epam_time = get_set_of_stock_prices('2020-07-28', '2020-08-16', 'EPAM', 'D')
# googl_time = get_set_of_stock_prices('2020-07-28', '2020-08-16', 'GOOGL', 'D')
# # msft_time = get_set_of_stock_prices('2020-07-28', '2020-08-16', 'MSFT', 'D')
# print(aapl_time, googl_time)
# # list_of_aapl_time = []
# list_of_epam_time = []
# for t in aapl_time:
#     list_of_aapl_time.append(convert_UTC_to_local_time(t))
# for t in epam_time:
#     list_of_epam_time.append(convert_UTC_to_local_time(t))
# print(list_of_aapl_time, list_of_epam_time)

# print(get_stock_information('AAC'))
# print(get_dict_of_companies_current_value_of_stocks('AAPL', 'EPAM'))
# print(count_current_value_of_all_stocks(get_dict_of_companies_current_value_of_stocks('AAPL', 'EPAM')))

# # Aggregate Indicators
# print(finnhub_client.aggregate_indicator('AAPL', 'D'))

# # Basic financials
# print(finnhub_client.company_basic_financials('AAPL', 'margin'))

# # Earnings surprises
# print(finnhub_client.company_earnings('TSLA', limit=5))

# # EPS estimates
# print(finnhub_client.company_eps_estimates('AMZN', freq='quarterly'))

# # Company Executives
# print(finnhub_client.company_executive('AAPL'))
#
# # Company News
# # Need to use _from instead of from to avoid conflict
# print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))
#
# # Company Peers
# print(finnhub_client.company_peers('AAPL'))
#
# # Company Profile
# print(finnhub_client.company_profile(symbol='AAPL'))
# print(finnhub_client.company_profile(isin='US0378331005'))
# print(finnhub_client.company_profile(cusip='037833100'))

# # Company Profile 2
# print(finnhub_client.company_profile2(symbol='AAPL'))
#
# # Revenue Estimates
# print(finnhub_client.company_revenue_estimates('TSLA', freq='quarterly'))
#
# # List country
# print(finnhub_client.country())
#
# # Crypto Exchange
# print(finnhub_client.crypto_exchanges())
#
# # Crypto symbols
# print(finnhub_client.crypto_symbols('BINANCE'))
#
# # Economic data
# print(finnhub_client.economic_data('MA-USA-656880'))
#
# # Filings
# print(finnhub_client.filings(symbol='AAPL', _from="2020-01-01", to="2020-06-11"))
#
# # Financials
# print(finnhub_client.financials('AAPL', 'bs', 'annual'))
#
# # Financials as reported
# print(finnhub_client.financials_reported(symbol='AAPL', freq='annual'))
#
# # Forex exchanges
# print(finnhub_client.forex_exchanges())
#
# # Forex all pairs
# print(finnhub_client.forex_rates(base='USD'))
#
# # Forex symbols
# print(finnhub_client.forex_symbols('OANDA'))
#
# # Fund Ownership
# print(finnhub_client.fund_ownership('AMZN', limit=5))
#
# # General news
# print(finnhub_client.general_news('forex', min_id=0))
#
# # Investors ownership
# print(finnhub_client.investors_ownership('AAPL', limit=5))
#
# # IPO calendar
# print(finnhub_client.ipo_calendar(_from="2020-05-01", to="2020-06-01"))
#
# # Major developments
# print(finnhub_client.major_developments('AAPL', _from="2020-01-01", to="2020-12-31"))
#
# # News sentiment
# print(finnhub_client.news_sentiment('AAPL'))
#
# # Pattern recognition+++++++
# print(finnhub_client.pattern_recognition('AAPL', 'D'))
#
# # Price target+++++++++
# print(finnhub_client.price_target('AAPL'))
#
# Quote

#
# # Recommendation trends++++++
# print(finnhub_client.recommendation_trends('AAPL'))
#
# # Stock dividends
# print(finnhub_client.stock_dividends('KO', _from='2019-01-01', to='2020-01-01'))
#
# # Stock symbols
# print(finnhub_client.stock_symbols('US')[0:5])
#
# # Transcripts
# print(finnhub_client.transcripts('AAPL_162777'))
#
# # Transcripts list
# print(finnhub_client.transcripts_list('AAPL'))
#
# # Earnings Calendar
# print(finnhub_client.earnings_calendar(_from="2020-06-10", to="2020-06-30", symbol="", international=False))
#
# # Covid-19
# print(finnhub_client.covid19())
#
# # Upgrade downgrade
# print(finnhub_client.upgrade_downgrade(symbol='AAPL', _from='2020-01-01', to='2020-06-30'))
#
# # Economic code
# print(finnhub_client.economic_code()[0:5])
#
# # Support resistance
# print(finnhub_client.support_resistance('AAPL', 'D'))
#
# # Technical Indicator
    # print(finnhub_client.technical_indicator(symbol="AAPL", resolution='D', _from=1583098857, to=1584308457, indicator='rsi', indicator_fields={"timeperiod": 3}))
#
# # Stock splits
# print(finnhub_client.stock_splits('AAPL', _from='2000-01-01', to='2020-01-01'))
#
# # Forex candles
# print(finnhub_client.forex_candles('AAPL', 'W', _from='2020-07-01', to='2020-08-01'))
#
# # Crypto Candles
# print(finnhub_client.crypto_candles('BINANCE:BTCUSDT', 'D', 1590988249, 1591852249))
#
# # Tick Data
# print(finnhub_client.stock_tick('AAPL', '2020-03-25', 500, 0))
#
#
# # Indices Constituents
# print(finnhub_client.indices_const(symbol = "^GSPC"))
#
# # Indices Historical Constituents
# print(finnhub_client.indices_hist_const(symbol = "^GSPC"))
#
# # ETFs Profile
# print(finnhub_client.etfs_profile('SPY'))
#
# # ETFs Holdings
# print(finnhub_client.etfs_holdings('SPY'))
#
# # ETFs Industry Exposure
# print(finnhub_client.etfs_ind_exp('SPY'))
#
# # ETFs Country Exposure
# print(finnhub_client.etfs_country_exp('SPY'))