import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")


chart1 = {
            "values": [16, 15, 12, 6, 5, 4, 42],
            "labels": [
                "US",
                "China",
                "European Union",
                "Russian Federation",
                "Brazil",
                "India",
                "Rest of World"
            ],
            "domain": {"x": [0, .48]},
            "name": "GHG Emissions",
            "hoverinfo": "label+percent+name",
            "hole": .4,
            "type": "pie"

        }

chart2 = {
            "values": [27, 11, 25, 8, 1, 3, 25],
            "labels": [
                "US",
                "China",
                "European Union",
                "Russian Federation",
                "Brazil",
                "India",
                "Rest of World"
            ],

            "domain": {"x": [.52, 1]},
            "name": "CO2 Emissions",
            "hoverinfo": "label+percent+name",
            "hole": .4,
            "type": "pie"

        }

trace0 = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name = "TFSA",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

trace1 = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "RRSP",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)

trace2 = go.Scatter(
                x=df.Date,
                y=df['AAPL.Close'],
                name = "Smart Saving",
                line = dict(color = '#F8B041'),
                opacity = 0.8)


pielayout = {
            'height': 500,
            'width': '100%',
        }

app = dash.Dash()
app.layout = html.Div([

    html.Div([
        html.H1("Black Swan", style={'color':'#ffffff', 'margin': 15}),
        html.H2("See what we've been up to", style={'color':'#caccce', 'margin': 15}),
    ], style={'backgroundColor':'#333333'}),

    html.Div([
        html.Div([
            dcc.Graph(
                id='g1',
                style={'margin': 30},
                figure={
                    'data': [chart1],
                    'layout': [pielayout],
                    'layout' : go.Layout(showlegend=False, autosize=True,
                                         margin=go.Margin(
                                             l=170,
                                             r=5,
                                             b=10,
                                             t=0,
                                             pad=0
                                         ),
                                         ),
                }
            )
        ], className="four columns"),

        html.Div([
            dcc.Graph(
                id='g2',
                style={'margin': 30},
                figure={
                    'data': [chart2],
                    'layout': [pielayout],
                    'layout': go.Layout(showlegend=False,
                                        margin=go.Margin(
                                             l=0,
                                             r=180,
                                             b=10,
                                             t=10,
                                             pad=0
                                         ),
                                        ),
                }
            )
        ],style={'border': '#333333'},className="four columns"),

        html.Div([
            dcc.Graph(
                id='g3',
                style={'margin': 30},
                figure={
                    'data': [chart2],
                    'layout': [pielayout],
                    'layout' : go.Layout(showlegend=False, autosize=True,
                                         margin=go.Margin(
                                             l=0,
                                             r=180,
                                             b=10,
                                             t=10,
                                             pad=0
                                         ),
                                         ),

                }
            )
        ], className="four columns"),

    ], className="row"),

    html.Div([
        dcc.Graph(
            id = 's1',
            style={'margin': 30},
            figure={
                'data': [trace0,trace1, trace2],
                "layout":dict(
                    title = "Portfolio value",
                    xaxis = dict(range = ['2016-07-01','2016-12-31'])
                )
            }
        )
    ])
    ], style={'backgroundColor':'#EEEEEE'})

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})



if __name__ == '__main__':
    app.run_server(debug=True)