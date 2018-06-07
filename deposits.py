import HelloController_py as api
import json

def deposits():
    j=json.loads(api.data_getter.get_data('account_assignments?account_id=rrsp-50dttgfe'))
    to_print = j['target_portfolio_id']
    print(to_print)

deposits()

