from api_handler import data_getter
from datetime import date, timedelta
from typing import List, Dict
import json


def get_dates(start: date, end: date, num_dates=10) -> List[date]:
    """
    Get a list of 10 days spread out in the interval

    It rounds to the nearest day
    """
    # Calculate the differences between the dates
    dates = []
    difference = end - start
    interval = difference.days / 10.0

    # Add a date every interval * i days
    for i in range(num_dates - 1):
        dates.append(start + timedelta(round(interval * i)))
    dates.append(end)

    return dates


def get_accounts() -> List[str]:
    """Get the list of accounts excluding the corporate accounts"""
    accounts = []
    data = data_getter.get_data('accounts')

    # Load data
    json_data = json.loads(data)
    results = json_data['results']

    # Add the accounts to the list, exclude the corporate accounts
    for result in results:
        if 'corporate' not in result['id']:
            accounts.append(result['id'])

    return accounts


def list_positions(id_: str, dates: List[date]) -> (Dict[date, List[float]], List[str], Dict[date, float]):
    """Get the porfolio holding percentage for each company"""
    symbols = []
    position_percentages = {}
    totals = {}

    # Send a request for each date
    for date in dates:
        values = []
        percentages = []
        sum_ = 0

        # Get the response from API
        parameters = {'account_id': id_, 'date': date}
        data = data_getter.get_data('positions', parameters=parameters)
        json_data = json.loads(data)
        results = json_data['results']

        # For each asset, parse the data
        for result in results:
            symbol = result['asset']['symbol']
            value = abs(float(result['book_value']['amount']))  # I only take positive book values

            # Record the symbol and values
            if symbol not in symbols:
                print("Adding %s to symbols" % symbol)
                symbols.append(symbol)
            values.append(value)
            sum_ += value
            totals[date] = sum_

        # Calculate the percentage for each asset
        for value in values:
            percentages.append(int((value / sum_) * 1000))
        position_percentages[date] = percentages

    return position_percentages, symbols, totals


def get_latest_deposit() -> Dict:
    """
    Return the latest deposit info in a dictionary

    'date' points to date object
    'amount' points to int

    Currently returns dummy data because get deposits does not seem to work
    """
    info = {'date': date(2018, month=6, day=20), 'amount': 1000}
    # params = {'start_date': '2017-01-01', 'end_date': '2018-12-12', 'limit': '250'}
    # data = data_getter.get_data('deposits', parameters=params)
    # print(data)
    return info


if __name__ == "__main__":
    data_getter.setup()  # You need this just to set up the data_getter
    dates = get_dates(date(2018, month=2, day=12), date(2018, month=4, day=23))  # This is how you enter the dates
    accounts = get_accounts()  # Get the list of accounts
    # for account in accounts:
        # print("### %s ###" % account)  # Print the account name
        # pp, s, t = list_positions(account, dates)  # pp is the dict of data to list of percentages
        # # s is list of corresponding symbols
        # # t is the list of totals of portfolio value
        #
        # print(pp)
        # print(s)
        # print(t)
    get_latest_deposit()
