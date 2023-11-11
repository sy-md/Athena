from dash import Dash, dcc, html, Input, Output
import pandas as pd

import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

available_countries = df['country'].unique()

app.layout = html.Div([
    dcc.Graph(
        id='clientside-graph'
    ),
    dcc.Store(
        id='clientside-figure-store',
        data=[{
            'x': df[df['country'] == 'Canada']['year'],
            'y': df[df['country'] == 'Canada']['pop']
        }]
    ),
    'Indicator',
    dcc.Dropdown(
        {'pop' : 'Population', 'lifeExp': 'Life Expectancy', 'gdpPercap': 'GDP per Capita'},
        'pop',
        id='clientside-graph-indicator'
    ),
    'Country',
    dcc.Dropdown(available_countries, 'Canada', id='clientside-graph-country'),
    'Graph scale',
    dcc.RadioItems(
        ['linear', 'log'],
        'linear',
        id='clientside-graph-scale'
    ),
    html.Hr(),
    html.Details([
        html.Summary('Contents of figure storage'),
        dcc.Markdown(
            id='clientside-figure-json'
        )
    ])
])


@app.callback(
    Output('clientside-figure-store', 'data'),
    Input('clientside-graph-indicator', 'value'),
    Input('clientside-graph-country', 'value')
)
def update_store_data(indicator, country):
    dff = df[df['country'] == country]
    return [{
        'x': dff['year'],
        'y': dff[indicator],
        'mode': 'markers'
    }]


app.clientside_callback(
    """
    function(data, scale) {
        return {
            'data': data,
            'layout': {
                 'yaxis': {'type': scale}
             }
        }
    }
    """,
    Output('clientside-graph', 'figure'),
    Input('clientside-figure-store', 'data'),
    Input('clientside-graph-scale', 'value')
)


@app.callback(
    Output('clientside-figure-json', 'children'),
    Input('clientside-figure-store', 'data')
)
def generated_figure_json(data):
    return '```\n'+json.dumps(data, indent=2)+'\n```'


if __name__ == '__main__':
    app.run_server(debug=True)
