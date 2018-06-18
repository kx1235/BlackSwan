import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

from datetime import date
from data import data_getter
from data.data_getter import list_positions, get_dates
from app import dates, total_rrsp, total_hisa, total_tfsa, date_end
from portfolio import *

'''
date_beg = date(2018, month=3, day=12)
date_end = date(2018, month=4, day=23)
dates = get_dates(date_beg, date_end)
'''
port_id = get_account()

tfsa_last = dates[3]
rrsp_last = dates[2]
hisa_last = dates[4]

days_tfsa = date_end - tfsa_last
days_rrsp = date_end - rrsp_last
days_hisa = date_end - hisa_last

'''
endpoint_tfsa = 'projections?account_id='+'tfsa-arbu_-o3'+'?amount=500?frequency=monthly?start_date='+tfsa_last
endpoint_rrsp = 'projections?account_id='+port_id[0]+'?amount=500?frequency=monthly?start_date='+rrsp_last
endpoint_hisa = 'projections?account_id='+port_id[2]+'?amount=500?frequency=monthly?start_date='+hisa_last
'''

'''
j1 = json.loads(api.data_getter.get_data(endpoint_tfsa))
print(j1)
proj_j1=j1['results']['data']['value']
j2 = json.loads(api.data_getter.get_data(endpoint_rrsp))
proj_j2=j2['results']['data']['value']
j3 = json.loads(api.data_getter.get_data(endpoint_hisa))
proj_j3=j3['results']['data']['value']
'''
y_tfsa = total_tfsa[dates[9]]
y_rrsp = total_rrsp[dates[9]]
y_hisa = total_hisa[dates[9]]

barGraph_tfsa = go.Bar(
    x=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    y=[y_tfsa, y_tfsa * 1.2, y_tfsa * 1.5],
    text=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

barGraph_rrsp = go.Bar(
    x=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    y=[y_rrsp, y_rrsp * 1.3, y_rrsp * 1.6],
    text=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

barGraph_hisa = go.Bar(
    x=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    y=[y_tfsa, y_hisa * 1.1, y_hisa * 1.3],
    text=['No deposit', 'Monthly Contribution of $500', 'Monthly Contribution + No Withdrawals'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

barLayout = go.Layout(
    autosize=False,
    width=570,
    height=500,
    margin=go.Margin(
        l=100,
        r=0,
        b=100,
        t=100,
        pad=7
    ),
    xaxis=dict(
        title=str(date_end),
        titlefont=dict(color='#dbdbdb'),
        linecolor='#dbdbdb',
        tickcolor='#dbdbdb',
        tickfont=dict(color='#dbdbdb'),
    ),

    yaxis=dict(
        linecolor='#dbdbdb',
        tickcolor='#dbdbdb',
        tickfont=dict(color='#dbdbdb'),
    ),

    paper_bgcolor='#333333',
    plot_bgcolor='#333333'
)
