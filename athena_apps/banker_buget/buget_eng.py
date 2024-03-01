import pandas as pd

data2 = [100,50,51,78,300]
data_time = [x for x in range(len(data2))] # this should be like time series data
trendline = [0 * i for i in data_time]

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


