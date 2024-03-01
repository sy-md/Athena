import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash import Dash,html,dcc
from buget_eng import *

colors = {
    "background": '#111111'
}

<<<<<<< HEAD
fig = make_subplots(rows=1,cols=2)

data2 = [1503,1500,1418,1253,1126]

def negtive_diff(tmp):
    print("neg {}%".format(round(((tmp[1] - tmp[0]) / tmp[0])* 100)))
    return round(((tmp[1] - tmp[0]) / tmp[0])* 100)

def postive_diff(tmp):
    print("pos {}%".format(round(((tmp[1] - tmp[0]) / tmp[1])* 100)))
    return round(((tmp[1] - tmp[0]) / tmp[1])* 100)

def find_trend(data):
    base = [x for x in range(len(data))]
    trendline = [1514 * 1 for _ in base]
    print("osl",trendline)
    return trendline

def test_fuc():
    cnt = 0
    tmp = []
    lst = []
    hold = 0
    for x in range(len(data2)):
        tmp.append(data2[x])
        cnt += 1
        if cnt == 2:
            print(tmp)
            if tmp[0] > tmp[1]:
                neg_num = negtive_diff(tmp)
                lst.append(int(neg_num))
            else:
                pos_num = postive_diff(tmp)
                lst.append(int(pos_num))
            hold = tmp.pop()
            tmp = []
            tmp = [hold]
            print("after reset",tmp)
            cnt = 1

    for j in range(1,len(lst)):
        nv = (lst[j-1] + lst[j])
        lst.pop()
        lst.append(nv)


    print("the list",lst)
    return lst
=======

fig = make_subplots(rows=1,cols=2)

<<<<<<< HEAD
=======
data2 = [100,50,51]
data_time = [x for x in range(len(data2))] # this should be like time series data
trendline = [0 * i for i in data_time]
>>>>>>> origin/TomorrowLand


#data_time = [0,1,2,3]
#trendline = [0,0,0,0]

def negtive_diff(tmp):
    print("neg",(((tmp[1] - tmp[0]) / tmp[0])* 100))
    return (((tmp[1] - tmp[0]) / tmp[0])* 100)

def postive_diff(tmp):
    print("pos",(((tmp[1] - tmp[0]) / tmp[1])* 100))
    return (((tmp[1] - tmp[0]) / tmp[1])* 100)

def find_trend(data):
    base = [x for x in range(len(data))]
    trendline = [0 * i for i in data_time]
    print("osl",trendline)
    return trendline

def test_fuc():
    cnt = 0
    tmp = []
    lst = []
    hold = 0
    for x in range(len(data2)):
        tmp.append(data2[x])
        cnt += 1
        if cnt == 2:
            print(tmp)
            if tmp[0] > tmp[1]:
                neg_num = negtive_diff(tmp)
                lst.append(neg_num)
            else:
                pos_num = postive_diff(tmp)
                lst.append(pos_num)
            hold = tmp.pop()
            tmp = []
            tmp = [hold]
            print("after reset",tmp)
            cnt = 1
    print("the list",lst)
    return lst

df = pd.DataFrame(dict(
    y = data2, #data
    t = find_trend(data2) #trendline
))

dfp = pd.DataFrame(dict(
    y = test_fuc(),# a even number of points 2,4,6
))


<<<<<<< HEAD
fig.add_trace( # the trendline
        go.Scatter(x=list([i for i in df.index.values]), y=df["t"], mode='lines',name="base amount"),
        row=1,col=1)

fig.add_trace( # user data
        go.Scatter(x=list([i for i in df.index.values]), y=df["y"], mode='lines', name="user data"),
        row=1,col=1)

fig.add_trace( # user percentage change
        go.Scatter(x=list([i for i in dfp.index.values]), y=dfp["y"], mode='lines', name="percentage"),
        row=1,col=2)

fig.add_trace( # the trendline
        go.Scatter(x=list([i for i in dfp.index.values]), y=list([i * 0 for i in df.index.values]), mode='lines', name="timeline"),
        row=1,col=2)


fig.update_layout(height=600,width=900)

#app.layout = html.Div(children=[
#    html.h1(children="fdhdfkjsdhf"),
#
#    dcc.Graph(
#        id="example1",
#        figure=fig
#    )
#])
#if __name__ == "__main__":
#    app.run(debug=True)
fig.show()
#print(df)
#print(dfp)


=======

>>>>>>> System/Athena
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
<<<<<<< HEAD
    app.run(debug=True)
    #fig.show()
=======
#    app.run(debug=True)
    fig.show()
#print(df)
#print(dfp)


>>>>>>> origin/TomorrowLand

#i should use two graphgs one for like the points of $600 and $300 so this will be twp points
#this  is also a 50% decrese to then then the other grpah will show the the point of 50% 
#then when the another point is added for example $300 + $150 then the next point on the perctenage grpah will
#be 25% so itll show 50% to 25% showing a negative trend line in percentages
>>>>>>> System/Athena
