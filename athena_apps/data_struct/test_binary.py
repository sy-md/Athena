class node:
    def __init__(self,val=None):
        self.val = val
        self.lf = None
        self.rt = None

class trees:
    def __init__(self):
        self.root = None


    def preorder(self):
        cur = self.root

        print(cur.val)

        while cur:
            cur = cur.lf
        print(cur.lf.val)


t = trees()

t.root = node(10)

t.root.lf = node(5)
t.root.rt = node(10)
t.root.lf.rt = node(8)
t.preorder()
