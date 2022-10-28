from dataclasses import dataclass

@dataclass
class Node:
    data: str
    Next: None

    def start():

        #build the indivual nodes
        Node.Next = ""
        a = Node([],Node.Next)
        b = Node([],Node.Next)
        c = Node([],Node.Next)
        d = Node([],Node.Next)

        #put data in desired node
        a.data.append("cat")

        #map them
        a.Next = b
#       b.Next = c
#       c.Next = d

        #excute featurte unpo uswr request [add,remove ect]
        print(a)
        print("")
        print("moving to the next link")
        x = a.data.pop()
        a.Next.data.append(x)
        print("")
        print(a)

#Node.start()
"""
class node : data next
class linked: dont know what operstiin i has


"""
