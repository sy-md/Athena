class graph:
    def __init__(self):
        self.map = {}

    def build(self,key,val):
        g = self.map
        """
        if key is already in the dict
        then take tue val and append i tot the list
        else make a key with its val
        """
        if key in g:
            g[key].append(val)
        else:
            g[key] = [val]

    def bfs(self,st,en):
        """
        put the starting pos in the q
        also long as as there is s9mething in q
        pop the first one and
            if pos has the poss of the dst point break
            check its possitbilites

        """
        q = []
        vis = []
        g = self.map

        q.append(st)
        while len(q) > 0:
            tmp = q.pop(0)

            if en in g[tmp]:
                vis.append(en)
                print("path:",vis)
                break

            for i in g[tmp]:
                print(i)
                q.append(i)

            vis.append(tmp)






t = graph()

t.build("home","bus1")
t.build("bus1","park")
t.build("home","arcade")
t.build("arcade","mall")
t.build("mall","bus2")
t.build("bus2","home")
t.build("park","bus2")

print(t.map)

t.bfs("arcade","park")

