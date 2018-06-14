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
                x=df.Date,
                y=df['AAPL.High'],
                name = "TFSA",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

trace1 = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "RRSP",
                line = dict(color = '#FFFFFF'),
                opacity = 0.8)

trace2 = go.Scatter(
                x=df.Date,
                y=df['AAPL.Close'],
                name = "Smart Saving",
                line = dict(color = '#F8B041'),
                opacity = 0.8)

portfolio_value = {
                        'data': [trace0,trace1, trace2],
                        "layout":dict(
                            title = "Portfolio value",
                            showlegend= False,
                            width = 200,
                            titlefont= dict(color='#dbdbdb'),
                            margin=go.Margin(
                                l=50,
                                r=40,
                                b=150,
                                t=100,
                                pad=7
                            ),
                            xaxis = dict(
                                range = ['2016-07-01','2016-12-31'],
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
                    style={'margin-left': 0, 'margin-bottom': 150},
                    figure= portfolio_value,
                )
            ], className="five columns"),

    ], className="row"),

], style={'backgroundColor':'#333333'})

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})



if __name__ == '__main__':
    app.run_server(debug=True)