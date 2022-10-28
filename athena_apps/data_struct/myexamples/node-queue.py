class node:
    def __init__(self,val=None):
        self.val = val
        self.n = None

class queuend:
    def __init__(self):
        self.q = []
        self.fr = 0
        self.r = -1
        self.count = 0

    def push(self,val):
        cur = self
        nd = node(val)

        if cur.fr is None:
            self.count += 1
            cur.q.insert(self.fr)
        else:
            cur.q.append(nd)
            self.count += 1

    def poping(self):
        tmp = self.q.pop(0)
        self.count -= 1
        print("removed",tmp.val)

    def display(self):
        print("amount",self.count)
        print("front",self.q[self.fr].val)
        print("rear",self.q[self.r].val)
        for x in self.q:
           print(x.val)

myq = queuend()

myq.push("martell")
myq.push("abby")
myq.push("kat")
myq.push("kelly")
myq.push("mark")
myq.display()
myq.poping()
myq.poping()
myq.poping()
myq.poping()
myq.push("jimmy")
myq.display()
"""
same things as node-stack

but for this one

top will be head
and tail will be the last


head -- 1
3
5
6
tail -- 8

every new node.next will be tail

"""
