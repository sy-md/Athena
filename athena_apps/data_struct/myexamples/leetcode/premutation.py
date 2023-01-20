class premutations:
    def __init__(self,data):
        self.nums = data
        self.tmp = []
        self.res = []

    def getFirst(self):
        first = 0
        while self.nums[first]:
            premutations.premute(self,self.nums[first])
            self.nums = self.nums[1:] + self.nums[:1]
            
    def premute(self,first):
        self.tmp.append(first)
        premutations.push(self,first)

    def push(self,first):
        for x in self.nums[first::]:
            self.tmp.append(x)

        self.res.append(self.tmp)
        self.tmp = []
        print(self.res)
        premutations.reversedPush(self,first)

    def reversedPush(self,first):
        self.tmp.append(first)
        rev = reversed(self.nums[first::])
        for x in rev:
            self.tmp.append(x)
  
        self.res.append(self.tmp)
        self.tmp = []
        print(self.res)
        
data = [1,2,3]
mypre = premutations(data)
mypre.getFirst()