from datetime import datetime
def date_get(list_dates):
    to_dates = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in list_dates]
    return [(date_str.day, date_str.month, date_str.year) for date_str in to_dates]


print(date_get(['2020-04-04','2020-07-12']))