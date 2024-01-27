import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

fig = go.Figure()

data2 = [3, 5, -2, 3, 4]
data_time = [x for x in range(max(data2))] # this should be like time series data
trendline = [0 * i for i in data_time]

df = pd.DataFrame(dict(
    x = data_time, #when
    y = data2 #amount
))


fig.add_trace(go.Scatter(x=data_time, y=trendline, mode='lines'))
fig.add_trace(go.Scatter(x=df["x"], y=df["y"], mode='lines')) #the orange line

fig.show()
print(df)


i should use two graphgs one for like the points of $600 and $300 so this will be twp points
this  is also a 50% decrese to then then the other grpah will show the the point of 50% 
then when the another point is added for example $300 + $150 then the next point on the perctenage grpah will
be 25% so itll show 50% to 25% showing a negative trend line in percentages
