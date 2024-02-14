import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, html, dcc
import pandas as pd

colors = {
    "background": '#111111'
}

# Load the CSV data
data = pd.read_csv('Testing.csv', sep=",")


fig = make_subplots(rows=1,cols=2)



fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['12Tempbt'], mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['10Tempbt'], mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['ChamberTempbt'], mode='lines'),
    row=1, col=1)



fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['12Temptc'], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['10Temptc'], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.Scatter(x=data['Time'], y=data['ChamberTemptc'], mode='lines'),
    row=1, col=2)


fig.update_layout(
    #height=600,width=900,
    #plot_bgcolor=colors['background'],
    #paper_bgcolor=colors['background'],
)

# Create a Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div(
    #style={'backgroundColor': colors['background']},

    children=[
        html.H1(children="fdhdfkjsdhf"),

    dcc.Graph(
        id="example1",
       figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

