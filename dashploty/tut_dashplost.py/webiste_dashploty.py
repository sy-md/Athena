from dash import Dash, dcc, html, Input, Output
import dash_enterprise_auth as auth

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server  # Expose the server variable for deployments

# Standard Dash app code below
app.layout = html.Div(className='container', children=[

    html.Div([
        html.H2('Sample App', id='header-title', className='ten columns'),
        html.Div(auth.create_logout_button(), className='two columns', style={'marginTop': 30})
    ]),
    html.Div(id='dummy-input', style={'display': 'none'}),

    html.Div([
        html.Div(
            className='four columns',
            children=[
                dcc.Dropdown(['LA', 'NYC', 'MTL'], 'LA', id='dropdown')
        ]),
        html.Div(
            className='eight columns',
            children=[
                dcc.Graph(id='graph')
            ])
    ])
])

@app.callback(Output('header-title','children'),
              Input('dummy-input', 'children'))
def update_title(_):

    # print user data to the logs
    print(auth.get_user_data())

    # update header with username
    return 'Hello {}'.format(auth.get_username())

@app.callback(Output('graph', 'figure'),
              Input('dropdown', 'value'))
def update_graph(value):
    return {
        'data': [{
            'x': [1, 2, 3, 4, 5, 6],
            'y': [3, 1, 2, 3, 5, 6]
        }],
        'layout': {
            'title': value,
            'margin': {
                'l': 60,
                'r': 10,
                't': 40,
                'b': 60
            }
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True)