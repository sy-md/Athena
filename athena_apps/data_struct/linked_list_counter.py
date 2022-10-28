import json as js
from time import sleep

file = "help.json"

with open(file, "w")as snd:
    js.dump([0],snd)


class node:
    def __init__(self,val):
        self.val = val
        self.nx = None

class llinked:
    def __init__(self):
        self.hd = None

    def insert(self,val):
        cur = self.hd
        new_node = node(val)

        if cur is None:
            cur = new_node

        while cur.nx:
            cur = cur.nx
        cur.nx = new_node

    def display(self):
        cur = self.hd

        with open (file,"r") as rd:
            data = js.load(rd)

            """
            it works beatifully ckunts 1 - nth nodes smoothly
            its counts to 1 -5
            """
            while cur:
                data[0] = cur.val
                cur = cur.nx
                sleep(1.2)
                print(data[0])
                with open(file, "w")as snd:
                    js.dump(data,snd)


l = llinked()
l.hd = node(0)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)

l.display()





