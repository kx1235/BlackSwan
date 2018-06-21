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
from postDeposit import *



class Data:
    def __init__(self, accounts, dates):
        self.accounts = accounts
        self.dates = dates

        self.rrsp = {dates[0]: []}, [], {}
        self.tfsa = {dates[0]: []}, [], {}
        self.hisa = {dates[0]: []}, [], {}

        self.y_rrsp = 0
        self.y_tfsa = 0
        self.y_hisa = 0

        self.y_rrsp_data = [self.y_rrsp, self.y_rrsp * 1.3, self.y_rrsp * 1.6]
        self.y_tfsa_data = [self.y_tfsa, (self.y_tfsa * 1.5), (self.y_tfsa * 1.9)]
        self.y_hisa_data = [self.y_hisa, self.y_hisa * 1.1, self.y_hisa * 1.3]

        # Create bar graphs
        self.barGraph_rrsp = go.Bar(
            x=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            y=self.y_rrsp_data,
            text=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            marker=dict(
                color=['rgb(242,72,241)', 'rgb(243,164,242)',
                       'rgb(232,26,152)']),
            opacity=1
        )

        self.barGraph_tfsa = go.Bar(
            x=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            y=self.y_tfsa_data,
            text=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            marker=dict(
                color=['rgb(46,126,78)', 'rgb(49,164,82)',
                       'rgb(51,214,66)']),
            opacity=1
        )

        self.barGraph_hisa = go.Bar(
            x=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            y=self.y_hisa_data,
            text=['Current Value', 'Monthly Deposit of $500', 'Monthly Deposit + No Withdrawals'],
            marker=dict(
                color=['rgb(47,129,183)', 'rgb(66,118,161)',
                       'rgb(62,204,203)']),
            opacity=1
        )

    def update(self):
        rrsp = list_positions(account1, dates)
        tfsa = list_positions(account2, dates)
        hisa = list_positions(account3, dates)

        # Deep copy
        for date in rrsp[0]:
            if date == self.dates[0]:
                for item in rrsp[0][date]:
                    self.rrsp[0][date].append(item)
            else:
                self.rrsp[0][date] = rrsp[0][date]
        for date in tfsa[0]:
            if date == self.dates[0]:
                for item in tfsa[0][date]:
                    self.tfsa[0][date].append(item)
            else:
                self.tfsa[0][date] = tfsa[0][date]
        for date in hisa[0]:
            if date == self.dates[0]:
                for item in hisa[0][date]:
                    self.hisa[0][date].append(item)
            else:
                self.hisa[0][date] = hisa[0][date]

        for symbol in rrsp[1]:
            self.rrsp[1].append(symbol)
        for symbol in tfsa[1]:
            self.tfsa[1].append(symbol)
        for symbol in hisa[1]:
            self.hisa[1].append(symbol)

        for date in rrsp[2]:
            self.rrsp[2][date] = rrsp[2][date]
        for date in tfsa[2]:
            self.tfsa[2][date] = tfsa[2][date]
        for date in hisa[2]:
            self.hisa[2][date] = hisa[2][date]

        self.y_rrsp = int(self.rrsp[2][dates[9]])
        self.y_tfsa = int(self.tfsa[2][dates[9]])
        self.y_hisa = int(self.hisa[2][dates[9]])

        self.y_rrsp_data.extend([self.y_rrsp, self.y_rrsp * 1.3, self.y_rrsp * 1.6])
        self.y_tfsa_data.extend([self.y_tfsa, (self.y_tfsa * 1.5), (self.y_tfsa * 1.9)])
        self.y_hisa_data.extend([self.y_hisa, self.y_hisa * 1.1, self.y_hisa * 1.3])

        self.y_rrsp_data.pop(0)
        self.y_rrsp_data.pop(0)
        self.y_rrsp_data.pop(0)
        self.y_tfsa_data.pop(0)
        self.y_tfsa_data.pop(0)
        self.y_tfsa_data.pop(0)
        self.y_hisa_data.pop(0)
        self.y_hisa_data.pop(0)
        self.y_hisa_data.pop(0)


date_beg = date(2018, month=3, day=12)
date_end = date(2018, month=4, day=23)

dates = get_dates(date_beg, date_end)

account1 = 'rrsp-50dttgfe'
account2 = 'tfsa-arbu_-o3'
account3 = 'ca-hisa-lciuw77c'

data = Data([account1, account2, account3], dates)

amount_rrsp, symbol_rrsp, total_rrsp = data.rrsp
amount_tfsa, symbol_tfsa, total_tfsa = data.tfsa
amount_hisa, symbol_hisa, total_hisa = data.hisa

x1=[dates[0]]
x2=[dates[0]]
x3=[dates[0]]

y1=[]
y2=[]
y3=[]

app = dash.Dash(url_base_pathname='/dash')



slider = dcc.Slider(
    id='slider',
    min=1,
    max=9,
    value=0,
    step=1,
    marks={
        0: dates[0],
        1: dates[1],
        2: dates[2],
        3: dates[3],
        4: dates[4],
        5: dates[5],
        6: dates[6],
        7: dates[7],
        8: dates[8],
        9: dates[9],
    },
)

nextbut = html.Button('Next', id='button', n_clicks=0)

fig1 = go.Layout(
    showlegend=False,
    autosize=False,
    width=470,
    height=450,
        margin=go.Margin(
            l=40,
            r=0,
            b=80,
            t=50,
            pad=1
        ),
    paper_bgcolor='#1D1D1D'
                  '',
    plot_bgcolor='#1D1D1D'
                 ''
    )

fig2 = go.Layout(
        showlegend=False,
        autosize=False,
    width=470,
    height=450,
        margin=go.Margin(
            l=0,
            r=40,
            b=80,
            t=50,
            pad=1
        ),
    paper_bgcolor='#1D1D1D'
                  '',
    plot_bgcolor='#1D1D1D'
                 '')

fig3 = go.Layout(
        showlegend=False,
        autosize=False,
    width=470,
    height=450,
        margin=go.Margin(
            l=0,
            r=40,
            b=80,
            t=50,
            pad=7
        ),
    paper_bgcolor='#1D1D1D'
                  '',
    plot_bgcolor='#1D1D1D'
                 ''
    )



trace0 = go.Scatter(
    x=x1,
    y=y1,
    name = "TFSA",
    line=dict(color='#FFFFFF'),
                opacity = 0.8)

trace1 = go.Scatter(
    x=x2,
    y=y2,
                name = "RRSP",
                line = dict(color = '#FFFFFF'),
                opacity = 0.8)

trace2 = go.Scatter(
    x=x3,
    y=y3,
    name="Smart Savings",
    line=dict(color='#FFFFFF'),
                opacity = 0.8)

portfolio_value = {
                        'data': [trace0,trace1, trace2],
                        "layout":dict(
                            title = "Portfolio value",
                            width = 300,
                            showlegend=True,
                            titlefont= dict(color='#dbdbdb'),
                            margin=go.Margin(
                                l=50,
                                r=40,
                                b=50,
                                t=100,
                                pad=7
                            ),
                            xaxis = dict(
                                range=dates,
                                showgrid= True,
                                gridcolor = '#898989',
                                linecolor='#dbdbdb',
                                tickcolor='#dbdbdb',
                                tickfont = dict(color='#dbdbdb'),

                            ),
                            yaxis = dict(
                                showgrid= True,
                                gridcolor = '#898989',
                                linecolor='#dbdbdb',
                                tickcolor='#dbdbdb',
                                tickfont = dict(color='#dbdbdb'),
                            ),
                            paper_bgcolor='#1D1D1D'
                                          '',
                            plot_bgcolor='#1D1D1D'
                        ),
                    }

tfsa_last = dates[3]
rrsp_last = dates[2]
hisa_last = dates[4]

days_tfsa = date_end - tfsa_last
days_rrsp = date_end - rrsp_last
days_hisa = date_end - hisa_last

barLayout = go.Layout(
    autosize=False,
    width=570,
    height=500,
    margin=go.Margin(
        l=100,
        r=150,
        b=200,
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

    paper_bgcolor='#1D1D1D',
    plot_bgcolor='#1D1D1D'
)

#####################DEPOSIT FEATURE#####################

input_amount = dcc.Input(id='amount-input', placeholder='$0.00', value='', type='number', )
drop_bank = dcc.Dropdown(
    id='drop_bank',
    options=[
        {'label': 'RBC****533', 'value': rbc533_id},
        {'label': 'RBC****453', 'value': rbc453_id},
        {'label': 'BMO****121', 'value': bmo121_id}
    ],
    value=rbc453_id)

radio_currency = dcc.RadioItems(
    id='currency',
    options=[
        {'label': 'CAD', 'value': 'CAD'},
        {'label': 'USD', 'value': 'USD'},
    ],
    value='CAD'
)

##########################################################



app.layout = html.Div([

    html.Div([
        html.H1("BLACK SWAN", style={'color': '#444ECC', 'margin': 20, },),
        html.H2("See what we've been up to", style={'color': '#444ECC', 'margin': 20}),
    ], style={'backgroundColor': '#1D1D1D'}, className='rows'),

    html.Div([
        html.Div([
            dcc.Graph(
                id='g1',
                figure={
                    'data': [{
                        "values": amount_tfsa[dates[0]],
                        "labels": symbol_tfsa,
                        'marker': {'colors':
                                       ['rgb(35, 104, 63)',
                                        'rgb(41, 165, 79)',
                                        'rgb(41, 127, 76)',
                                        'rgb(82, 214, 129)',
                                        'rgb(41, 127, 76)'
                                        'rgb(13, 211, 94)'
                                        'rgb(41, 165, 79)'
                                        'rgb(0, 173, 124)',
                                        'rgb(37, 216, 54)',
                                        'rgb(41, 165, 79)'
                                        'rgb(19, 142, 31)',
                                        'rgb(13, 211, 94)'
                                        'rgb(108, 168, 61)',
                                        'rgb(221, 199, 74)',
                                        ]},
                        "domain": {"x": [0, .48]},
                        "text": symbol_tfsa,
                        "textfont": dict(color='#DDDDDD'),
                        "hoverinfo": "none",
                        "hole": .4,
                        "type": "pie"
                    }, go.Pie(marker=dict(colors='colors'))],
                    'layout': fig1,
                }
            )
        ], className="two columns"),

        html.Div([
            dcc.Graph(
                id='g2',
                style={'margin-left': 60},
                figure={
                    'data': [{
                        "values": amount_rrsp[dates[0]],
                        "labels": symbol_rrsp,
                        'marker': {'colors':
                                       ['rgb(234, 5, 153)',
                                        'rgb(154, 15, 152)',
                                        'rgb(57, 6, 90)',
                                        'rgb(244, 61, 244)',
                                        'rgb(244, 162, 244)',
                                        'rgb(106, 5, 114)',
                                        'rgb(234, 6, 234)',
                                        'rgb(163, 70, 163)',
                                        'rgb(170, 67, 170)'
                                        ]},
                        "domain": {"x": [0, .48]},
                        "text": symbol_rrsp,
                        "textfont": dict(color='#DDDDDD'),
                        "hoverinfo": "none",
                        "hole": .4,
                        "type": "pie"
                    }, go.Pie(marker=dict(colors='colors'))],
                    'layout':fig2,
                }
            )
        ],className="two columns"),

        html.Div([
            dcc.Graph(
                id='g3',
                style={'margin-left': 70},
                figure={
                    'data': [{
                        "values": amount_hisa[dates[0]],
                        "labels": symbol_hisa,
                        'marker': {'colors':
                                       ['rgb(44, 62, 80)',
                                        'rgb(41, 128, 185)',
                                        'rgb(51, 204, 204)',
                                        'rgb(64, 118, 163)',
                                        'rgb(234, 155, 191)',
                                        'rgb(124, 82, 124)',
                                        'rgb(87, 87, 147)'
                                        ]},
                        "domain": {"x": [0, .48]},
                        "text": symbol_hisa,
                        "textfont": dict(color='#caccce'),
                        "hoverinfo": "none",
                        "hole": .4,
                        "type": "pie"
                    }, go.Pie(marker=dict(colors='DDDDDD'))],
                    'layout': fig3,
                }
            ),
        ], className="three columns"),

        html.Div([
                dcc.Graph(
                    id = 's1',
                    style={'margin-left': 0, 'margin-bottom': 50, 'height': 350,},
                    figure= portfolio_value,
                    animate=False
                )
            ], className="five columns"),

    ], className="row"),

    html.Div([
        html.Div(slider),
    ], style={"margin-left": 40, "margin-right": 40, }),

    html.Div([
        html.Div(nextbut),
    ], style={"margin-top": 30, "margin-left": 40, "margin-bottom": 100, "backgroundColor": "#F8B041", "width": 95}),

    html.Div([
        html.Div([

            html.Div([
                dcc.Dropdown(
                    id='drop',
                    options=[
                        {'label': 'TFSA', 'value': 'TFSA'},
                        {'label': 'RRSP', 'value': 'RRSP'},
                        {'label': 'Smart Savings', 'value': 'Smart Savings'}
                    ],
                    value='TFSA',
                ),
            ], style={"margin-left": 20}),
            html.Div([
                dcc.Graph(
                    id='bar1',
                    figure={
                        'data': [data.barGraph_tfsa],
                        'layout': barLayout
                    },
                )
            ]),

        ], className="five columns"),

        html.Div([
            html.Div([
                html.H4("Time since last deposit:", style={'color': '#F8B041', 'margin-left': 100})
            ], className="six columns"),

            html.Div(
                id='dayssince',
                children=html.H4('{}'.format(days_tfsa), style={'color': '#ffffff', 'margin-left': 30, }),
                className="six columns", style={"margin-top": 5}),
        ], className="five columns"),

        html.Div([
            html.Div([
                html.H4("What you missed out on:", style={'color': '#F8B041', 'margin-left': 100})
            ], className="six columns"),

            html.Div(
                id='missed',
                children=html.H4('${}'.format(round((data.y_tfsa * 1.9) - data.y_tfsa), 2),
                                 style={'color': '#ffffff', 'margin-left': 40})
                , className="six columns", style={"margin-top": 5}),
        ], className="five columns"),

        html.Div([
            html.Div(html.H4("Make a deposit"), style={'color': '#F8B041', 'margin-left': 100}),
            html.Div([
                html.Div(input_amount),
            ], style={'margin-top': 20, 'margin-left': 100}),
            html.Div([
                html.Div(drop_bank),
            ], style={'margin-top': 20, 'margin-left': 100}),
            html.Div([
                html.Div(radio_currency),
            ], style={'color': "#FFFFFF", 'margin-top': 20, 'margin-left': 100}),
            html.Div(html.H5(id='deposit-sentence'), style={'color': '#FFFFFF', 'margin-left': 100}),
            html.Div(html.H5(id='deposit-result'), style={'color': "#f9db43", 'margin-left': 100}),
            html.Div([
                html.Button('Deposit now', id="deposit")
            ], style={"margin-top": 40, 'margin-bottom': 50, 'margin-left': 100, 'backgroundColor': '#F8B041',
                      "width": 151})

        ], className="five columns")

    ], className="row"),
], style={'backgroundColor': '#1D1D1D', 'margin': 0, 'font-family': 'Helvetica'}, )

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})



@app.callback(
    Output('slider', 'value'),
    [Input('button', 'n_clicks')])
def update_slider(clicks):
    print('slider triggered')
    return clicks


@app.callback(
    Output('g1', 'figure'),
    [Input('button', 'n_clicks')])
def update_g1(clicks):
    print('g1 triggered')
    new_figure = {
        'data': [{
            "values": amount_rrsp[dates[clicks]],
            "labels": symbol_rrsp,
            'marker': {'colors':
                           ['rgb(35, 104, 63)',
                            'rgb(41, 165, 79)',
                            'rgb(41, 127, 76)',
                            'rgb(82, 214, 129)',
                            'rgb(41, 127, 76)'
                            'rgb(13, 211, 94)'
                            'rgb(41, 165, 79)'
                            'rgb(0, 173, 124)',
                            'rgb(37, 216, 54)',
                            'rgb(41, 165, 79)'
                            'rgb(19, 142, 31)',
                            'rgb(13, 211, 94)'
                            'rgb(108, 168, 61)',
                            'rgb(221, 199, 74)',
                            ]},
            "domain": {"x": [0, .48]},
            "text": symbol_rrsp,
            "textfont": dict(color='#DDDDDD'),
            "hoverinfo": "none",
            "hole": .4,
            "type": "pie"

        }],
        'layout': fig1
    }
    return new_figure


@app.callback(
    Output('g2', 'figure'),
    [Input('button', 'n_clicks')])
def update_g2(clicks):
    print('g2 triggered')
    new_figure = {
        'data': [{
            "values": amount_tfsa[dates[clicks]],
            "labels": symbol_tfsa,
            'marker': {'colors':
                           ['rgb(234, 5, 153)',
                            'rgb(154, 15, 152)',
                            'rgb(106, 5, 114)',
                            'rgb(57, 6, 90)',
                            'rgb(244, 61, 244)',
                            'rgb(244, 162, 244)'
                            'rgb(234, 6, 234)',
                            'rgb(163, 70, 163)',
                            'rgb(170, 67, 170)'
                            ]},
            "domain": {"x": [0, .48]},
            "text": symbol_tfsa,
            "textfont": dict(color='#DDDDDD'),
            "hoverinfo": "none",
            "hole": .4,
            "type": "pie"

        }],
        'layout': fig2
    }
    return new_figure


@app.callback(
    Output('g3', 'figure'),
    [Input('button', 'n_clicks')])
def update_g3(clicks):
    print('g3 triggered')
    new_figure = {
        'data': [{
            "values": amount_hisa[dates[clicks]],
            "labels": symbol_hisa,
            'marker': {'colors':
                           ['rgb(44, 62, 80)',
                            'rgb(41, 128, 185)',
                            'rgb(51, 204, 204)',
                            'rgb(64, 118, 163)',
                            'rgb(234, 155, 191)',
                            'rgb(124, 82, 124)',
                            'rgb(87, 87, 147)'
                            ]},
            "text": symbol_hisa,
            "textfont": dict(color='#DDDDDD'),
            "hoverinfo": "none",
            "domain": {"x": [0, .48]},
            "hole": .4,
            "type": "pie"

        }],
        'layout': fig3
    }
    return new_figure


@app.callback(
    Output('s1','figure'),
    [Input('button','n_clicks')])
def update_s1(clicks):
    x1.append(dates[clicks])
    x2.append(dates[clicks])
    x3.append(dates[clicks])

    y1.append(total_tfsa[x1[clicks]])
    y2.append(total_rrsp[x2[clicks]])
    y3.append(total_hisa[x3[clicks]])

    trace_tfsa=go.Scatter(
        x=x1,
        y=y1,
        name = "TFSA",
        line=dict(color='#58D584'),
        opacity = 0.8)

    trace_rrsp = go.Scatter(
        x=x2,
        y=y2,
        name="RRSP",
        line=dict(color='#A249A1'),
        opacity=1)

    trace_hisa = go.Scatter(
        x=x3,
        y=y3,
        name="Smart Savings",
        line=dict(color='#3ECCCB'),
        opacity=0.8)

    return {
                        'data': [trace_tfsa,trace_rrsp, trace_hisa],
                        "layout":dict(
                            title = "Portfolio value",
                            showlegend= False,
                            width=550,
                            titlefont= dict(color='#dbdbdb'),
                            margin=go.Margin(
                                l=50,
                                r=40,
                                b=50,
                                t=100,
                                pad=7
                            ),
                            xaxis = dict(
                                range=x1,
                                showgrid= True,
                                gridcolor = '#898989',
                                linecolor='#dbdbdb',
                                tickcolor='#dbdbdb',
                                tickfont = dict(color='#dbdbdb'),

                            ),
                            yaxis = dict(
                                showgrid= True,
                                gridcolor = '#898989',
                                linecolor='#dbdbdb',
                                tickcolor='#dbdbdb',
                                tickfont = dict(color='#dbdbdb'),
                            ),
                            paper_bgcolor='#1D1D1D',
                            plot_bgcolor='#1D1D1D'
                        ),
                    }


@app.callback(
    Output('bar1', 'figure'),
    [Input('drop', 'value')])
def update_bar(val):
    if val == 'TFSA':
        return {
            'data': [data.barGraph_tfsa],
            'layout': barLayout
        }
    elif val == 'RRSP':
        return {
            'data': [data.barGraph_rrsp],
            'layout': barLayout
        }
    elif val == 'Smart Savings':
        return {
            'data': [data.barGraph_hisa],
            'layout': barLayout
        }


@app.callback(
    Output('dayssince', 'children'),
    [Input('drop', 'value')])
def update_days(val):
    if val == 'TFSA':
        return html.H4('{}'.format(days_tfsa), style={'color': '#ffffff', 'margin': 40})
    elif val == 'RRSP':
        return html.H4('{}'.format(days_rrsp), style={'color': '#ffffff', 'margin': 40})
    elif val == 'Smart Savings':
        return html.H4('{}'.format(days_hisa), style={'color': '#ffffff', 'margin': 40})


@app.callback(
    Output('missed', 'children'),
    [Input('drop', 'value')])
def update_miss(val):
    if val == 'TFSA':
        return html.H4('${}'.format(round((data.y_tfsa * 1.9) - data.y_tfsa), 2),
                       style={'color': '#ffffff', 'margin': 40})
    elif val == 'RRSP':
        return html.H4('${}'.format(round((data.y_rrsp * 1.6) - data.y_rrsp), 2),
                       style={'color': '#ffffff', 'margin': 40})
    elif val == 'Smart Savings':
        return html.H4('${}'.format(round((data.y_hisa * 1.3) - data.y_hisa), 2),
                       style={'color': '#ffffff', 'margin': 40})


@app.callback(
    Output('deposit-result', 'children'),
    [Input('deposit', 'n_clicks')],
    [State('amount-input', 'value'), State('drop_bank', 'value'), State('currency', 'value'), State('drop', 'value')]
)
def update_result(clicks, amount, bank, currency, account):
    print(amount)
    print(currency)
    print(account)
    print(bank)
    print(get_personid())
    if account == 'TFSA':
        account_id = 'tfsa-arbu_-o3'
    if account == 'RRSP':
        account_id = 'rrsp-50dttgfe'
    if account == 'Smart Savings':
        account_id = 'ca-hisa-lciuw77c'
    deposit_request(amount, currency, bank, account_id, get_personid())
    if clicks > 0:
        return 'Success! Check your WealthSimple account for deposit pending status'


@app.callback(
    Output('deposit-sentence', 'children'),
    [Input('amount-input', 'value'), Input('drop_bank', 'value'), Input('currency', 'value'), Input('drop', 'value')]
)
def update_sentence(amount, bank, currency, account):
    if bank == rbc453_id:
        label = 'RBC****453'
    elif bank == rbc533_id:
        label = 'RBC****533'
    elif bank == bmo121_id:
        label = 'BMO****121'
    return 'Deposit ${} {} from {} into your {} account?'.format(amount, currency, label, account)

if __name__ == '__main__':

    app.run_server(debug=True)