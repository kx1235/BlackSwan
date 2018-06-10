import HelloController_py as api
import json
from pprint import pprint

def get_account():

    #converts json to python dict
    j= json.loads(api.data_getter.get_data('accounts?account_types=ca_tfsa,ca_rrsp,ca_hisa'))
    ids = j['results']
    count = j['total_count']
    account_list = []
    #for every object in results, append the account id to account_list
    for account in ids:
         account_list.append((account['id']))

    for id in account_list:
        print(id)


    return account_list

#return target portfolio id for each account
def get_portfolio_id():
    target_list=[]
    for id in get_account():
        endpoint = "account_assignments?account_id="+id
        k = json.loads(api.data_getter.get_data(endpoint))
        target_list.append(k['target_portfolio_id'])
    return target_list

for x in get_portfolio_id():
    print(x)

