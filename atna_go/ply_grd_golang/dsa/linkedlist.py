class Node:
    def __init__(self,data):
        self.data = data
        self.nx = None

class mylist:
    def __init__(self):
        self.head = None

    def insert(self, val):
        nd = Node(val)
        p = self.head

        if self.head == None:
            self.head = nd
        else:
            while p.nx != None:
                p = p.nx
            p.nx = nd




if __name__ == "__main__":
    kk = mylist()
    kk.insert(1)
    kk.insert(2)
    kk.insert(3)
    print("{}".format(kk.head.data))
    print("{}".format(kk.head.nx.data))
    print("{}".format(kk.head.nx.nx.data))