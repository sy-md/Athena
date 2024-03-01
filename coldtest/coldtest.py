import plotly.graph_objects as go
from plotly.subplots import make_subplots
<<<<<<< HEAD
from dash import dcc, html, Dash

app = Dash(__name__)

fig = make_subplots(rows=1, cols=2)
=======
from dash import Dash, html, dcc
from coldtest_eng import *

########## Create a Dash app ##########
app = Dash(__name__)

colors = {
    'background': '#2e2b28',
    'text': '#76c8c8'
}

fig.update_layout(
    height=1200,
    width=1200,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
>>>>>>> bc56eeb2a5cee14108eb24a9686d936cea3b1370

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
<<<<<<< HEAD
        id='example-graph',
=======
        id="example1",
>>>>>>> bc56eeb2a5cee14108eb24a9686d936cea3b1370
        figure=fig
    )
])

<<<<<<< HEAD
=======
#### Run the app ####
>>>>>>> bc56eeb2a5cee14108eb24a9686d936cea3b1370
if __name__ == '__main__':
    app.run_server(debug=True)