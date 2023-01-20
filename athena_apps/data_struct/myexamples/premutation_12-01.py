#premutation implentations [1,2,3]
class premu:
    def __init__(self,nums):
        self.nums = nums # [1,2,3]
        self.holder = []
        self.res = [[1,2,3]]

    def getPremutations(self):
        self.holder.append(self.nums)
        while self.holder != None:
            self.res.append(self.holder)
            self.holder = []
            #self.nums.pop()
            self.holder.append(self.nums[0])
            self.nums.append(self.holder[0])
            break

        print("ans", self.res )
        print("tmp is",self.holder )
            




data = [1,2,3]
test1 = premu(data)
test1.getPremutations()