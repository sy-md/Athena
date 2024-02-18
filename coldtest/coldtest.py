import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash, html, dcc
import pandas as pd
import pprint

colors = {
    "background": '#2e2b28',
    "text": '#76c8c8'
}

file1 = "Cold_Testing_Without_internet.csv"
file2 = "Cold_Testing_40C_W_Internet.csv"

# Load the CSV data
data = pd.read_csv(file1, sep=",")
data2 = pd.read_csv(file2, sep=",")

#the doctionary for the data

bluetooth_temp = {
    #data
    '12Temp_bt_d1': data['12" Temp (BT)'],
    '10Temp_bt_d1': data['10" Temp (BT)'], 
    'ChamberTemp_bt_d1': data['Chamber Temp (BT)'],
    #data2
    '12Temp_bt_d2': data2['12" Temp (BT)'],
    '10Temp_bt_d2': data2['10" Temp (BT)'],
    'ChamberTemp_bt_d2': data2['Chamber Temp (BT)']
}
thermocouple_temp = {
    #data
    '12Temp_tc_d1': data['12" Temp (TC-4)'],
    '10Temp_tc_d1': data['10" Temp (TC-3)'],
    'ChamberTemp_tc_d1': data['Chamber Temp (TC-2)'],
    #data2
    '12Temp_tc_d2': data2['12" Temp (TC-4)'],
    '10Temp_tc_d2': data2['10" Temp (TC-3)'],
    'ChamberTemp_tc_d2': data2['Chamber Temp (TC-2)']
}
cpu_temp = {
    #data
    '12Temp_cpu_d1': data['12" Temp (CPU)'],
    '10Temp_cpu_d1': data['10" Temp (CPU)'],
    #data2
    '12Temp_cpu_d2':data2['12" Temp (CPU)'],
    '10Temp_cpu_d2': data2['10" Temp (CPU)'],
}
heater_current = {
    #data
    '12Current_d1': data['12" Current'],
    '10Current_d1': data['10" Current'],
    #data2
    '12Current_d2': data2['12" Current'],
    '10Current_d2': data2['10" Current'],
}

fig = make_subplots(rows=4,cols=2)

# row 1 with cols 1 bluetooth temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["12Temp_bt_d1"], name='12" bt',mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["10Temp_bt_d1"], mode='lines'),
    row=1, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=bluetooth_temp["chambertemp_bt_d1"], mode='lines'),
    row=1, col=1)

### row 1 with cols 2 thermocouple temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["12Temp_tc_d1"], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["chambertemp_tc_d1"], mode='lines'),
    row=1, col=2)

fig.add_trace( 
    go.scatter(x=data['Time'], y=thermocouple_temp["chambertemp_tc_d1"], mode='lines'),
    row=1, col=2)

### row 2 with cols 1 cpu temp
fig.add_trace( 
    go.scatter(x=data['Time'], y=cpu_temp["12Temp_cpu_d1"], mode='lines'),
    row=2, col=1)

fig.add_trace( 
    go.scatter(x=data['Time'], y=cpu_temp["10Temp_cpu_d1"], mode='lines'),
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
    go.scatter(x=data2['Time'], y=bluetooth_temp["12Temp_bt_d2"], mode='lines'),
    row=3, col=1)

fig.add_trace( 
    go.scatter(x=data2['Time'], y=bluetooth_temp["10Temp_bt_d2"], mode='lines'),
    row=3, col=1)

fig.add_trace(
    go.scatter(x=data2['Time'], y=bluetooth_temp["chambertemp_bt_d2"], mode='lines'),
    row=3, col=1)

### row 3 with cols 2 thermocouple temp
fig.add_trace( 
    go.scatter(x=data2['Time'], y=thermocouple_temp["12Temp_tc_d2"], mode='lines'),
    row=3, col=2)

fig.add_trace( 
    go.scatter(x=data2['Time'], y=thermocouple_temp["chambertemp_tc_d2"], mode='lines'),
    row=3, col=2)

fig.add_trace(
    go.scatter(x=data2['Time'], y=thermocouple_temp["chambertemp_tc_d2"], mode='lines'),
    row=3, col=2)

### row 4 with cols 1 cpu temp
fig.add_trace(
    go.scatter(x=data2['Time'], y=cpu_temp["12Temp_cpu_d2"], mode='lines'),
    row=4, col=1)

fig.add_trace(
    go.scatter(x=data2['Time'], y=cpu_temp["10Temp_cpu_d2"], mode='lines'),
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

