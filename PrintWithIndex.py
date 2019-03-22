class PrintWithIndex:
    def __init__(self):
        self.n=int(input())
        self.narr=input()
        self.narr=[int(i) for i in self.narr.split()]

    def Printing(self):
        for i in range(0,self.n):
            if(i==self.n-1):
                print(self.narr[i],end=" ")
                print(i,end="")
            else:
                print(self.narr[i],end=" ")
                print(i)

pwi=PrintWithIndex()
pwi.Printing()
