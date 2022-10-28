"""
t = [[°°°°°°],
      °°°°°°
      °°°°°°
      °°°°°° ]
this will be a list of list - you got this
"""

class mazegame:
    def __init__(self):
        self.maze = [   ["•","w","w","w","w","w","w","w"],
                        ["t","w","°","°","°","°","°","°"],
                        ["°","w","°","w","°","°","w","°"],
                        ["°","°","°","w","°","w","°","°"],
                        ["w","w","°","w","°","w","w","°"],
                        ["f","w","°","w","°","°","w","°"],
                        ["°","w","w","w","w","w","°","°"],
                        ["°","°","°","°","°","°","°","°"] ]

        self.flag = self.maze[5][0]

    def board(self):
        maze = self.maze

        for x in maze:
            print(x,end="\n")

    def search(self):
        flg = self.flag
        mz = self.maze

        self.board()
        tmp = mz[1][0]
        print(tmp)
        mz[0][1] = tmp 
        self.board()

mze = mazegame()

mze.search()
