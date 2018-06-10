import HelloController_py as api
import json

def holdings():
    j=json.loads(api.data_getter.get_data('target_portfolios/target_portfolio-Rf9cuo_iWZurFWpQe3SuRutg'))
    #to_print = j['percent_equities']
    print(j)

holdings()

