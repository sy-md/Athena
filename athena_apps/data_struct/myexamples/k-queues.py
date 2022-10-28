class node:
    def __init__(self,val=None):
        self.val = val
        self.nx = None

class myq:
    def __init__(self,k,n):
        self.ques = [[] for _ in range(0,k)]
        self.cap = n

    def display(self,num):
        for i in self.ques[num]:
            print(i.val)
        print("list:",num)

    def insert(self,val):
        que = self.ques #k list
        cap = self.cap # cap
        nd = node(val) # node

        if len(que[0]) == 0:
            que[0].append(nd)
        else:
            i = 0
            que[0].insert(0,nd)
            que[0][0].nx = que[0][1]

            while len(que[0]) == cap:
               tmp = que[0].pop()
               que[2].append(tmp)



t = myq(3,3) # nums of k in q and cap



t.insert("kelly")
t.insert("mark")
t.insert("martell")
t.insert("jared")
t.insert("lilly")
t.insert("willy")
t.insert("emma")


t.display(0)
t.display(1)
t.display(2)


