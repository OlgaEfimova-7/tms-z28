from datetime import datetime, timedelta, timezone


def convert_string_date_to_datetime(date):
    list_of_date = list(map(int, date.split('-')))
    processed_date = datetime(list_of_date[0], list_of_date[1], list_of_date[2], 8, 30)
    return processed_date


def create_list_of_dates_between_start_and_final_date_without_vacations(start_date, finish_date):
    list_of_dates = []
    processed_start_date = convert_string_date_to_datetime(start_date)
    processed_finish_date = convert_string_date_to_datetime(finish_date)
    delta_days = processed_finish_date-processed_start_date
    for i in range(delta_days.days):
        date = processed_start_date+timedelta(days=i)
        if date.weekday() != 5 and date.weekday() != 6:
            list_of_dates.append(date.date())
    return list_of_dates


def convert_UTC_to_local_time(utc_dt):
    timestamp = datetime.fromtimestamp(utc_dt)
    return timestamp.strftime('%Y-%m-%d')


def convert_local_time_to_UTC(local_time):
    utc = int(local_time.replace(tzinfo=timezone.utc).timestamp())
    return utc


def is_second_date_bigger_then_first(first_date, second_date):
    first_date_datetime = convert_string_date_to_datetime(first_date)
    second_date_datetime = convert_string_date_to_datetime(second_date)
    return second_date_datetime >= first_date_datetime
