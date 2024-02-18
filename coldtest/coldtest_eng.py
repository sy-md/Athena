import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, html, dcc
import pandas as pd
import pprint
from coldtest import * 
from coldtest import bluetooth_temp, thermocouple_temp
fig = make_subplots(rows=4,cols=2)

# row 1 with cols 1 bluetooth temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["12temp_bt_d1"], name='12" bt',mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["10temp_bt_d1"], mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["chambertemp_bt_d1"], mode='lines'),
    row=1, col=1)

### row 1 with cols 2 thermocouple temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["12temp_tc_d1"], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["chambertemp_tc_d1"], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["chambertemp_tc_d1"], mode='lines'),
    row=1, col=2)

### row 2 with cols 1 cpu temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=cpu_temp["12temp_cpu_d1"], mode='lines'),
    row=2, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=cpu_temp["10temp_cpu_d1"], mode='lines'),
    row=2, col=1)

### row 2 with cols 2 current
fig.add_trace( 
    go.scatter(x=data['Time'], y=heater_current["12current_d1"], mode='lines'),
    row=2, col=2)

fig.add_trace(
    go.scatter(x=data['Time'], y=heater_current["10current_d1"], mode='lines'),
    row=2, col=2)

# row 3 with cols 1 bluetooth temp
fig.add_trace( 
    go.scatter(x=data2['Time'], y=bluetooth_temp["12temp_bt_d2"], mode='lines'),
    row=3, col=1)

fig.add_trace( 
    go.scatter(x=data2['Time'], y=bluetooth_temp["10temp_bt_d2"], mode='lines'),
    row=3, col=1)

fig.add_trace(
    go.scatter(x=data2['Time'], y=bluetooth_temp["chambertemp_bt_d2"], mode='lines'),
    row=3, col=1)

### row 3 with cols 2 thermocouple temp
fig.add_trace( 
    go.scatter(x=data2['Time'], y=thermocouple_temp["12temp_tc_d2"], mode='lines'),
    row=3, col=2)

fig.add_trace( 
    go.scatter(x=data2['Time'], y=thermocouple_temp["chambertemp_tc_d2"], mode='lines'),
    row=3, col=2)

fig.add_trace(
    go.scatter(x=data2['Time'], y=thermocouple_temp["chambertemp_tc_d2"], mode='lines'),
    row=3, col=2)

### row 4 with cols 1 cpu temp
fig.add_trace(
    go.scatter(x=data2['Time'], y=cpu_temp["12temp_cpu_d2"], mode='lines'),
    row=4, col=1)

fig.add_trace(
    go.scatter(x=data2['Time'], y=cpu_temp["10temp_cpu_d2"], mode='lines'),
    row=4, col=1)

### row 4 with cols 2 current
fig.add_trace(
    go.scatter(x=data2['Time'], y=heater_current["12current_d2"], mode='lines'),
    row=4, col=2)

fig.add_trace(
    go.scatter(x=data2['Time'], y=heater_current["10current_d2"], mode='lines'),
    row=4, col=2)

fig.update_layout(
    #height=1200,width=2000,
    height=1200,width=800,
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


# Create a Dash app
app = Dash(__name__)

# Define the layout
app.layout = html.Div(
    style={'backgroundColor': colors['background']},

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
