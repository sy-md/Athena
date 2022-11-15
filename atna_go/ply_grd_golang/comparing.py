# filler for go package 
#import
# i like coding

class kids: # classs
    def __init__(self,name,toy):
        self.name = name
        self.toy = toy

    def who(self):
        print("my name is {} and my fav toy is {}".format(self.name,self.toy))

class house:
    def __init__(self,lsname,kids):
        self.lname = {lsname : {kids.name : kids.toy}}

    def family(self):
        print(self.lname)

if __name__ == "__main__": # driver code
    kd1 = kids("jarry","plane") # obj
    kd2 = kids("harry","car")

    #family 1
    hood = house("dorsett",kd1)
    hood.family()
    kd1.who()

    #family 2
    hood = house("hodes",kd2)
    hood.family()
    kd2.who()
