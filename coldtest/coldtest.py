import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import dcc, html, Dash

app = Dash(__name__)

fig = make_subplots(rows=1, cols=2)

trace1 = fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
), row = 1, col = 1)

trace2 = fig.add_trace(go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
), row = 1, col = 2)

data: list = [trace1, trace2]

app.layout = html.Div(

    children=[html.H1("Hello Dash"),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)