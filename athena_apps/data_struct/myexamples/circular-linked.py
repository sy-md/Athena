class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self.prev = None

class linked:
    def __init__(self):
        self.head = None
    """
    have the end node connect to 
    first node
    """
    def insert(self,val):
        cur = self.head
        prev = None
        nd = node(val)

        if cur is None:
            cur = nd
        else:
            while cur.next:
                cur = cur.next
            cur.next = nd
            nd.next = cur



l = linked()

l.head = node("start")
l.insert("a")


print("test")
print(l.head.val)
print(l.head.next.val)
print(l.head.next.next.val)
