class eightqueenchessboard:
    def __init__(self):
        self.boardinfo=[-1,-1,-1,5,-1,3,-1,-1]
        self.step = 5

    def checkvalid(self):
        for i in range(self.step):
            if self.boardinfo[i] == -1:
                continue
            for j in range(i+1,self.step+1):
                if self.boardinfo[j] == -1:
                    continue
                if self.boardinfo[i] == self.boardinfo[j]:
                    return False
                elif self.boardinfo[i]-self.boardinfo[j] == i-j or self.boardinfo[j]-self.boardinfo[i]==i-j:
                    return False
        return True

    def printboard(self):
        for i in range(8):
            for j in range(8):
                if j==self.boardinfo[i]:
                    print("1 ",end="")
                else:
                    print("0 ",end="")
            print("\n" ,end="")

    def setqueen(self,i,j):
        self.boardinfo[i] = j



if __name__ == '__main__':
    print("hello world")

    a = eightqueenchessboard()
    a.printboard()
    print(a.checkvalid())