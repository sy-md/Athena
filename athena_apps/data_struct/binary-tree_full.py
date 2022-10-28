"""
BINARY TREE FULL IMP
********************
1.) display the tree
        • left and right tree
        • double tree

2.) add node base of hi or low
        • base off another condition
        • add to left or right nx avaiable

3.) add node at certain node
        • if complete tree add node
        to next avaiable child loc

4.) searching:
    • who is trg parent
    • who is trg grandparent
    • who child is trg
    • who grandson is trg

5.) delete node:
        • parent
        • child
        • cousin
        • sibiling

6.) level traversal:
        • list[list]
7.) bfs
    • dfs

"""
class node:
    def __init__(self,val):
        self.val = val
        self.l = None
        self.r = None
        self.nx = None

class binarytree:
    def __init__(self,root1,root2):
        self.root = [ node(root1),node(root2) ]

    def doubleTree(self,n): #connects root nodes
        self.root[0].nx = self.root[1]
        if n == 2:
            print(self.root[0].nx.val)
        print(self.root[0].val)

    def display(self,n): #level traversal
        q1,q2 = [self.root[n]],[]
        lv = []

        while len(q1) > 0:
            tk = q1.pop()
            if tk.l:
                q1.append(tk.l)
            if tk.r:
                q1.append(tk.r)
            if tk.val < self.root[n].val:
                q2.insert(0,tk)
            else:
                q2.append(tk)

        print([i.val for i in q2])

    def insert(self,n,val=None):
        cur = self.root[n]
        nd = node(val)

        if n+1 == 1:
            if val < cur.val:
                if cur.l == None:
                    cur.l = nd
                else:
                    cur.l.insert(n)
            else:
                if cur.r == None:
                    cur.r = nd
                else:
                    cur.l.insert(n)
        if n+1 == 2:
            pass

t = binarytree(10,"dorsett")
print("displaying roots")
print("root nodes", [x.val for x in t.root])
print("************")
t.insert(0,9)
t.insert(0,8)
print("displaying")
t.display(0)
