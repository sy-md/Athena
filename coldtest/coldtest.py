import plotly.graph_objects as go
from plotly.subplots import make_subplots
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

    children=[
        html.H1(children="fdhdfkjsdhf"),

    dcc.Graph(
        id="example1",
        figure=fig
    )
])

#### Run the app ####
if __name__ == '__main__':
    app.run_server(debug=True)

