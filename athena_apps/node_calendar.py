"""
calendar 


jan 31 feb 28 mar 31 apr 30


node 
    next
    date
    task

"""




class node: # day
    def __init__(self,int):
        self.task = []
class month: 
    def __init__(self,node):
        self.title = ""
        self.days = [node]
        self.next_month = None

class calendar:
    def __init__(self):
        self.year = "2022"

    def gen_month(self):
        cnt = 0 
        months = ["january","february","march","April"]
        days = [31,28,31,30]
        while cnt < len(months): 
            mkdz = month([node(i.__init__) for i in range(days[cnt])])
            print(mkdz.days)
            cnt += 1

      



my_cal = calendar()

print(my_cal.gen_month())



