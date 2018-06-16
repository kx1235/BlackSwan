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


dates = get_dates(date(2018, month=3, day=12), date(2018, month=4, day=23))

account1 = 'rrsp-50dttgfe'
rrsp = list_positions(account1, dates)
amount_rrsp, symbol_rrsp, total_rrsp = rrsp

account2 = 'tfsa-arbu_-o3'
tfsa = list_positions(account2, dates)
amount_tfsa, symbol_tfsa, total_tfsa = tfsa

account3 = 'ca-hisa-lciuw77c'
hisa = list_positions(account3, dates)
amount_hisa, symbol_hisa, total_hisa = hisa

x1 = [dates[0]]
x2 = [dates[0]]
x3 = [dates[0]]

y1 = [total_tfsa[x1[0]]]
y2 = [total_rrsp[x2[0]]]
y3 = [total_hisa[x3[0]]]


app = dash.Dash()
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

slider = dcc.Slider(
    id='slider',
    min=0,
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
    }
)

nextbut = html.Button('Next', id='button')

chart1 = {
            "values": [16, 15, 12, 6, 5, 4, 42],
            "labels": [
                "US",
                "China",
                "European Union",
                "Russian Federation",
                "Brazil",
                "India",
                "Japan"
            ],
            "domain": {"x": [0, .48]},
            "hoverinfo": "label+percent",
            "hole": .4,
            "type": "pie"

        }

fig1 = go.Layout(
        showlegend=False,
        autosize=False,
        width=570,
        height=400,
        margin=go.Margin(
            l=40,
            r=50,
            b=100,
            t=100,
            pad=1
        ),
        paper_bgcolor='#333333',
        plot_bgcolor='#333333'
    )

fig2 = go.Layout(
        showlegend=False,
        autosize=False,
        width=570,
        height=400,
        margin=go.Margin(
            l=0,
            r=50,
            b=100,
            t=100,
            pad=1
        ),
        paper_bgcolor='#333333',
        plot_bgcolor='#333333')

fig3 = go.Layout(
        showlegend=False,
        autosize=False,
        width=570,
        height=400,
        margin=go.Margin(
            l=0,
            r=0,
            b=100,
            t=100,
            pad=7
        ),
        paper_bgcolor='#333333',
        plot_bgcolor='#333333'
    )



trace0 = go.Scatter(
    x=x1,
    y=y1,
                name = "TFSA",
                line = dict(color = '#17BECF'),
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
                name = "Smart Saving",
                line = dict(color = '#F8B041'),
                opacity = 0.8)

portfolio_value = {
                        'data': [trace0,trace1, trace2],
                        "layout":dict(
                            title = "Portfolio value",
                            showlegend= False,
                            width=300,
                            titlefont= dict(color='#dbdbdb'),
                            margin=go.Margin(
                                l=50,
                                r=40,
                                b=150,
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
                            paper_bgcolor='#333333',
                            plot_bgcolor='#333333'
                        ),
                    }

app = dash.Dash()
app.layout = html.Div([

    html.Div([
        html.H1("Black Swan", style={'color':'#ffffff', 'margin': 20}),
        html.H2("See what we've been up to", style={'color':'#caccce', 'margin': 20}),
    ], style={'backgroundColor':'#333333'}),

    html.Div([
        html.Div([
            dcc.Graph(
                id='g1',
                figure={
                    'data':[chart1],
                    'layout': fig1,
                }
            )
        ],className="two columns"),

        html.Div([
            dcc.Graph(
                id='g2',
                style={'margin-left': 60},
                figure={
                    'data': [chart1],
                    'layout':fig2,
                }
            )
        ],className="two columns"),

        html.Div([
            dcc.Graph(
                id='g3',
                style={'margin-left': 70},
                figure={
                    'data': [chart1],
                    'layout': fig3,
                }
            )
        ], className="three columns"),

        html.Div([
                dcc.Graph(
                    id = 's1',
                    style={'margin-left': 0, 'margin-bottom': 150, 'height': 600},
                    figure= portfolio_value,
                    animate=False
                )
            ], className="five columns"),

    ], className="row"),

    html.Div(slider),
    html.Div(nextbut),
], style={'backgroundColor': '#333333'}, )

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
            "domain": {"x": [0, .48]},
            "hoverinfo": "label+percent",
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
    print('g1 triggered')
    new_figure = {
        'data': [{
            "values": amount_tfsa[dates[clicks]],
            "labels": symbol_tfsa,
            "domain": {"x": [0, .48]},
            "hoverinfo": "label+percent",
            "hole": .4,
            "type": "pie"

        }],
        'layout': fig1
    }
    return new_figure


@app.callback(
    Output('g3', 'figure'),
    [Input('button', 'n_clicks')])
def update_g3(clicks):
    print('g1 triggered')
    new_figure = {
        'data': [{
            "values": amount_hisa[dates[clicks]],
            "labels": symbol_hisa,
            "domain": {"x": [0, .48]},
            "hoverinfo": "label+percent",
            "hole": .4,
            "type": "pie"

        }],
        'layout': fig1
    }
    return new_figure


@app.callback(
    Output('s1', 'figure'),
    [Input('button', 'n_clicks')])
def update_s1(clicks):
    x1.append(dates[clicks])
    x2.append(dates[clicks])
    x3.append(dates[clicks])

    y1.append(total_tfsa[x1[clicks]])
    y2.append(total_rrsp[x2[clicks]])
    y3.append(total_hisa[x3[clicks]])

    trace_tfsa = go.Scatter(
        x=x1,
        y=y1,
        name="TFSA",
        line=dict(color='#17BECF'),
        opacity=0.8)

    trace_rrsp = go.Scatter(
        x=x2,
        y=y2,
        name="RRSP",
        line=dict(color='#FFFFFF'),
        opacity=0.8)

    trace_hisa = go.Scatter(
        x=x3,
        y=y3,
        name="Smart Saving",
        line=dict(color='#F8B041'),
        opacity=0.8)

    return {
        'data': [trace_tfsa, trace_rrsp, trace_hisa],
        "layout": dict(
            title="Portfolio value",
            showlegend=False,
            width=300,
            titlefont=dict(color='#dbdbdb'),
            margin=go.Margin(
                l=50,
                r=40,
                b=150,
                t=100,
                pad=7
            ),
            xaxis=dict(
                range=x1,
                showgrid=True,
                gridcolor='#898989',
                linecolor='#dbdbdb',
                tickcolor='#dbdbdb',
                tickfont=dict(color='#dbdbdb'),

            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='#898989',
                linecolor='#dbdbdb',
                tickcolor='#dbdbdb',
                tickfont=dict(color='#dbdbdb'),
            ),
            paper_bgcolor='#333333',
            plot_bgcolor='#333333'
        ),
    }





if __name__ == '__main__':
    app.run_server(debug=True)