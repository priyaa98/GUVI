class SortNum:
    def __init__(self):
        self.n=int(input())
        self.narr=input()
        self.narr=[int(i) for i in (self.narr).split(" ")]

    def PrintSorted(self):
        self.narr.sort()
        for i in range(0,len(self.narr)):
            if(i==len(self.narr)-1):
                print(self.narr[i])
            else:
                print(self.narr[i],end=" ")

p=SortNum()
p.PrintSorted()
