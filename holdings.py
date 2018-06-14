import HelloController_py as api
import json


# function that will retrieve a list of lists
# [[list-of-symbols],[list-of,amounts]]
def holdings(account_id, date):
    # creates endpoint
    endpoint = 'positions?account_id=' + account_id + '?date=' + date
    j = json.loads(api.data_getter.get_data(endpoint))
    # enters the dictionary to parse data
    entry_point = j['results']
    # print(entry_point)

    # creates a list of symbols
    symbol_list = []
    for symbol in entry_point:
        symbol_list.append(symbol['asset']['symbol'])
        #print(symbol)

    # creates a list of amounts respective to the list of symbols above, index 0 of symbol_list corresponds to index 0 of amount_list
    amount_list = []
    for amount in entry_point:
        amount_list.append(amount['book_value']['amount'])
        #print(amount)

    # packages symbol_list and amount_list into another list so only single return needed.
    # eliminates need to repeat endpoint call
    data_list = []
    data_list.append(symbol_list)
    data_list.append(amount_list)

    return data_list


'''
NOT SURE WHY ENTERING A DATE RETURNS AN EMPTY JSON, IF YOU TAKE OUT THE DATE SO IT IS ONLY ACCOUNT ID PARAMETER
EVERYTHING WILL WORK.
MAY BE API ISSUE, OTHERWISE PLEASE FIX
'''

test = holdings('rrsp-50dttgfe', '2018-06-12')

for i in test:
    for x in i:
        print(x)
