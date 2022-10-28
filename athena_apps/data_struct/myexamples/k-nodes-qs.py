class node:
    def __init__(self,val):
        self.nx = None
        self.val = val

class myq:
    def __init__(self):
        self.head = None
        self.tail = node("start")
        self.dst = node("store")

        self.st = []
        self.tmp = []

    def display(self):
        cur = self.tail
        dst = self.dst
        """
        with the capitcy of the 2nd q
        in till index is 0
        print each node - minus the cap
        """

        i = len(self.tmp)
        while i >= 0:
            print(cur.val,"-->",end="")
            cur = cur.nx
            cur = self.tmp[i-1]
            i -= 1

        print(dst.val)

    def insert(self,val):
        cur = self.tail
        st = self.st
        tmp = self.tmp

        """
        given a array print it backwards

        take even number and turn it into a node
        move to first q
        then poo to next q
        REVERSED
        """
        for i in val:
            nd = node(i)
            st.append(nd)
            tk = st.pop()
            tmp.append(tk)


t = myq() # nums of k in q and cap


y = [1,2,3,4,5]
t.insert(y)
t.display()


