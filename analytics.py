import os

import matplotlib.pyplot as plt
from finnhub import FinnhubAPIException

from hash_and_coding import decoding_str
from requests_of_inf_about_stock_market import get_current_value_of_stocks


def is_float(value):
    try:
        return float(value)
    except ValueError:
        return False


def get_list_of_decoded_companies_and_stocks(list_of_companies_and_stocks):
    final_list_with_decoded_information = []
    for list_of_one_db_row in list_of_companies_and_stocks:
        internal_list_of_db_row = [decoding_str(i) for i in list_of_one_db_row]
        internal_list_of_db_row_int_converted = []
        for index, elem in enumerate(internal_list_of_db_row):
            if index == 1 or index == 2:
                int_elem = float(elem)
                internal_list_of_db_row_int_converted.append(int_elem)
            else:
                internal_list_of_db_row_int_converted.append(elem)
        final_list_with_decoded_information.append(internal_list_of_db_row_int_converted)
    return final_list_with_decoded_information


def get_list_of_aggregated_companies_and_stocks(list_of_companies_and_stocks):
    list_of_companies_name = [list_of_row[0] for list_of_row in list_of_companies_and_stocks]
    set_of_companies_name = set(list_of_companies_name)
    final_list = []
    if len(list_of_companies_name) == len(set_of_companies_name):
        final_list = list_of_companies_and_stocks
    else:
        for company in set_of_companies_name:
            if list_of_companies_name.count(company) > 1:
                list_of_row = []
                all_amount_of_stocks = sum(list(row[1] for row in list_of_companies_and_stocks if row[0] == company))
                all_initial_sum_of_investments = sum(list(row[2] for row in list_of_companies_and_stocks if row[0] ==
                                                          company))
                currency = list_of_companies_and_stocks[list_of_companies_name.index(company)][3]
                list_of_row.append(company)
                list_of_row.append(all_amount_of_stocks)
                list_of_row.append(all_initial_sum_of_investments)
                list_of_row.append(currency)
                final_list.append(list_of_row)

            else:
                for row in list_of_companies_and_stocks:
                    if company in row:
                        final_list.append(row)
                        break
    return final_list


def analyze_value_of_stocks(list_of_companies_and_stocks: list, list_of_sold_companies_stocks=[[0, 0, 0, 0, 0]]):
    list_with_current_value_of_stocks = []
    list_of_companies_which_stocks_sold = [i for i in list_of_sold_companies_stocks[0]]
    for i in list_of_companies_and_stocks:
        list_with_current_value_of_stocks.append(list(i))
    # Get current value of stocks and set to final list
    try:
        dict_of_company_and_current_value_of_stocks = {}
        for i in list_with_current_value_of_stocks:
            company = i[0]
            amount_of_stocks = i[1]
            current_value_of_one_stock = get_current_value_of_stocks(company)
            if company not in list_of_companies_which_stocks_sold:
                i.append(current_value_of_one_stock*amount_of_stocks)
                dict_of_company_and_current_value_of_stocks[company] = (amount_of_stocks, current_value_of_one_stock)
            else:
                amount_of_sold_stocks = list_of_sold_companies_stocks[list_of_companies_which_stocks_sold.index(
                    company)][1]
                price_of_sold_stocks = list_of_sold_companies_stocks[list_of_companies_which_stocks_sold.index(
                    company)][2]
                i.append(current_value_of_one_stock*(amount_of_stocks-amount_of_sold_stocks) + price_of_sold_stocks)
                dict_of_company_and_current_value_of_stocks[company] = (amount_of_stocks-amount_of_sold_stocks,
                                                                        current_value_of_one_stock)

        # Calculate initial value and current value of all stocks, create final list with company and delta of stock
        # value
        initial_value = 0
        current_value_of_actual_stocks = 0
        final_list = []
        arrow_up = u'\u21E7'
        arrow_down = u'\u21E9'
        for i in list_with_current_value_of_stocks:
            current_value_of_company_stocks = i[4]
            initial_value_of_company_stocks = i[2]
            if (current_value_of_company_stocks-initial_value_of_company_stocks) > 0:
                final_list.append(f"{i[0]} --> +{round(current_value_of_company_stocks-initial_value_of_company_stocks, 2)} {arrow_up}")
            else:
                final_list.append(f"{i[0]} --> {round(current_value_of_company_stocks-initial_value_of_company_stocks, 2)} {arrow_down}")
            for index_j, j in enumerate(i):
                company = i[0]
                if company not in list_of_companies_which_stocks_sold:
                    if index_j == 2:
                        initial_value += j
                    elif index_j == 4:
                        current_value_of_actual_stocks += j
                else:
                    if index_j == 2:
                        initial_value += i[2] - list_of_sold_companies_stocks[list_of_companies_which_stocks_sold.index(
                            company)][2]
                    elif index_j == 4:
                        current_value_of_actual_stocks += (dict_of_company_and_current_value_of_stocks[company])[0] \
                                                          * (dict_of_company_and_current_value_of_stocks[company])[1]
        final_row = '\n'.join(final_list)
        delta = 0
        if (current_value_of_actual_stocks - initial_value) > 0:
            delta = f'+{round(current_value_of_actual_stocks - initial_value, 2)} {arrow_up}'
        else:
            delta = f'{round(current_value_of_actual_stocks - initial_value, 2)} {arrow_down}'
        return f'Первоначальные инвестиции: {round(initial_value, 2)}\nРыночная стоимость акций: {round(current_value_of_actual_stocks, 2)}'\
               f'\nДельта: {delta}\n\nИзменения стоимости акций компаний:\n{final_row}'
    except FinnhubAPIException:
        return 'На данный момент сервер перегружен. Попробуй через минуту'


def calculate_set_of_stock_price_delta(initial_value_of_stocks, amount_of_stocks,
                                       list_of_historical_data_of_stock_prices, sold_value_of_stocks=0):
    list_of_historical_data_of_stock_prices_with_consideration_of_amount = []
    for elem in list_of_historical_data_of_stock_prices:
        if elem is not None:
            new_elem = elem*amount_of_stocks+sold_value_of_stocks
            list_of_historical_data_of_stock_prices_with_consideration_of_amount.append(new_elem)
        else:
            list_of_historical_data_of_stock_prices_with_consideration_of_amount.append(None)
    final_list_of_stock_price_delta = []
    for elem in list_of_historical_data_of_stock_prices_with_consideration_of_amount:
        if elem is not None:
            new_elem = elem - initial_value_of_stocks
            final_list_of_stock_price_delta.append(new_elem)
        else:
            final_list_of_stock_price_delta.append(None)
    return final_list_of_stock_price_delta


def calculate_set_of_stock_price_delta_of_several_companies(list_of_delta):
    zipped_list = zip(*list_of_delta)
    final_list = []
    for elem in zipped_list:
        if None not in elem:
            final_list.append(sum(elem))
        else:
            final_list.append(sum(filter(None.__ne__, elem)))
    return final_list


def create_list_of_data_from_several_lists(list_of_lists_of_dates):
    final_list = None
    max_len_of_list = max(list(len(i) for i in list_of_lists_of_dates))
    for list_of_date in list_of_lists_of_dates:
        if len(list_of_date) == max_len_of_list:
            final_list = list_of_date
        break
    return final_list


def create_set_of_data_subject_to_no_data_for_some_dates(list_of_lists_of_data, list_of_lists_of_dates,
                                                         final_list_of_date):
    for index_list, list_of_dates in enumerate(list_of_lists_of_dates):
        if len(list_of_dates) != len(final_list_of_date):
            list_of_index_of_dates_with_no_data = []
            for index, elem in enumerate(final_list_of_date):
                if elem not in list_of_dates:
                    list_of_index_of_dates_with_no_data.append(index)
            for index in list_of_index_of_dates_with_no_data:
                list_of_lists_of_data[index_list].insert(index, None)
    return list_of_lists_of_data


def remove_file(chat_id):
    if os.path.exists(f'graphics/graph_{chat_id}.png'):
        os.remove(f'graphics/graph_{chat_id}.png')


def draw_graphics(list_of_data_sets, list_of_companies, list_of_dates, chat_id):
    for index, list_of_data in enumerate(list_of_data_sets):
        plt.plot(list_of_dates, list_of_data, label=list_of_companies[index])
        plt.legend()
    plt.xticks(rotation=90)
    plt.title(f'Динамика прибыли/убытка как разность между рыночной \nстоимостью акций и ценой покупки акций')
    plt.grid()
    remove_file(chat_id)
    plt.savefig(f'graphics/graph_{chat_id}.png')
    plt.show()

