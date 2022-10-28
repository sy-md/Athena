ls1 = [1,3,5,4,2]
# >> 1,2,3,4,5 sorted
# >> 2,4,1,3,5 evens first

class myq:
    def __init__(self,lst=None):
        self.stk1 = []
        self.stk2 = []
        self.tmpstk = []

    def display(self,lst):
        print("orignal",lst)

    def sorted(self,lst): # >> 1,2,3,4,5 sorted
        res = []
        f = 0
        l = -1
        while len(res) < 5:
            if lst[f] < lst[l]:
                res.append(lst[f])
                f += 1
            else:
                res.append(lst[l])
                l += -1
        print(res)

    def seperated(self,lst):# >> 2,4,1,3,5 evens first
        stk1 = self.stk1
        stk2 = self.stk2

        for i in lst:
            if i % 2:
                stk2.append(i)
            else:
                stk1.append(i)

        print(self.stk1)
        print(self.stk2)
        for i in stk2:
            stk1.append(i)
        print("seperated",self.stk1)

stk = myq()

stk.display(ls1)
print("displaying even then odds")
stk.seperated(ls1)
print("displaying in skrted order")
stk.sorted(ls1)




