import plotly.graph_objects as go

fig = go.Figure()
data_time = [0, 1, 2, 3, 4] # this should be like time series data
data2 = [3, 5, -2, 3, 4]
trendline = [0 * i for i in data_time] 
# this is the trendline, it is a list of 0's the same length as the data list
fig.add_trace(go.Scatter(x=data_time, y=trendline, mode='lines'))
fig.add_trace(go.Scatter(x=data_time, y=data2, mode='lines')) #the orange line

fig.show()
