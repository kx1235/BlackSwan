from datetime import date

from data import data_getter
from data.data_getter import list_positions, get_dates

account = 'rrsp-50dttgfe'
dates = get_dates(date(2018, month=3, day=12), date(2018, month=4, day=23))
a = list_positions(account, dates)

percent, symbol, total = a

print(percent[dates[1]])

print(symbol)

print(dates[0])
