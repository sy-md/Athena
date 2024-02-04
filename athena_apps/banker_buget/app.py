import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash,html,dcc
from buget_eng import *

colors = {
    "background": '#111111'
}


fig = make_subplots(rows=1,cols=2)

fig.add_trace( # the trendline
        go.Scatter(x=list([i for i in df.index.values]), y=df["t"], mode='lines'),
        row=1,col=1)

fig.add_trace( # user data
        go.Scatter(x=list([i for i in df.index.values]), y=df["y"], mode='lines'),
        row=1,col=1)

fig.add_trace( # user percentage change
        go.Scatter(x=list([i for i in dfp.index.values]), y=dfp["y"], mode='lines'),
        row=1,col=2)

fig.add_trace( # the trendline
        go.Scatter(x=list([i for i in dfp.index.values]), y=list([i * 0 for i in df.index.values]), mode='lines'),
        row=1,col=2)

fig.update_layout(
    #height=600,width=900,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
)

# the html of the dash app
app = Dash(__name__)

app.layout = html.Div(
    style={'backgroundColor': colors['background']},

    children=[
        html.H1(children="fdhdfkjsdhf"),

    dcc.Graph(
        id="example1",
       figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
    #fig.show()
