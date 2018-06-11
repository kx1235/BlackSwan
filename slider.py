import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([

    html.Div(dcc.Slider(
        id='slider',
        min=0,
        max=10,
        value=0,
        step=1,
        )),
    html.Button('next',id='nextbut')])



@app.callback(
    dash.dependencies.Output('slider','value'),
    [dash.dependencies.Input('nextbut','n_clicks')])
def update_slider(value):
    return value+1


if __name__ == '__main__':
    app.run_server(debug=True)
