# given so sorted shit make a effeicnt way to find shit
class speed:
    def __init__(self,size,skip):
        self.arr = [ _ for _ in range(0,size,skip) ]

    def display(self):
        print(self.arr)

    def firstalgo(self,num):
        arr = self.arr
        s = 0
        # O(N)
        for x in range(0,len(arr)):
            s += 1
            if arr[x] < num:
                x += 1
            else:
                arr.insert(x,num)
                break

        print("answer 1",s)
#        algo.display()


    def secalgo(self,num):
        arr = self.arr
        i = 0
        j = len(arr)-1
        s1 = 0
        # o(n^2)
        while arr[i] != arr[j]:
            s1 += 1
            if arr[i+1] != arr[j]:
                i += 1
                j-=1
                if arr[i] > num:
                    arr.insert(i-1,num)
                    break
                if arr[j] < num:
                    arr.insert(j+1,num)
                    break
            else:
                arr.insert(j-1,num)
                break

        print("answer 2",s1)
#        algo.display()


    def binarysrch(self,num):
        arr = self.arr
        st = 0
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        while True:
            if right[st] > num:
                right.insert(st,num)
                left.append(right)
                break
            st += 1
        algo.display()
        print(right)


algo = speed(20,2)

algo.display()

num = 11
#algo.firstalgo(num)
#algo.secalgo(num)
algo.binarysrch(num)
