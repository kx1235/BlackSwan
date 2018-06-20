import requests

import api_handler as api
import json
from pprint import pprint
from api_handler import creds

# no account_name to know which bank
rbc533_id = 'bank_account-NOSMqWq17OqwzdxCA2rB2gA2LNw'
rbc453_id = 'bank_account-UOmUMkBVkdHxbZkyTTkYcAw7ZsQ'
bmo121_id = 'bank_account-r9csRpcyhbOvTKSnCGbbcoNs3w'


def get_personid():
    j = json.loads(api.data_getter.get_data('people'))
    id_person = j['results'][0]['id']
    return id_person


def get_person_name():
    j = json.loads(api.data_getter.get_data('people/' + get_personid()))
    name = j['full_legal_name']['first_name']
    return name



def deposit_request(amount, currency, bank, port, client):
    endpoint = "https://api.sandbox.wealthsimple.com/v1/deposits"
    headers = {'Authorization': 'Bearer %s' % creds['access_token']}
    data = {
        "client_id": client,
        "bank_account_id": bank,
        "account_id": port,
        "amount": amount,
        "currency": currency

    }

    r = requests.post(url=endpoint, headers=headers, data=data)

    response = r.text
    print(response)
