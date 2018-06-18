import api_handler as api
import json
from pprint import pprint

def get_account():

    #converts json to python dict
    j = json.loads(api.data_getter.get_data('accounts?account_types=ca_tfsa,ca_rrsp,ca_hisa'))
    ids = j['results']
    count = j['total_count']
    account_list = []
    #for every object in results, append the account id to account_list
    for account in ids:
         account_list.append((account['id']))

    for id in account_list:
        print(id)

    return account_list

#def get_portfolio_id(id_list):




get_account()

