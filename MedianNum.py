class MedianNum:
    def __init__(self):
        self.n=int(input())
        self.narr=input()
        self.narr=[int(i) for i in (self.narr).split(" ")]

    def PrintMedian(self):
        self.narr.sort()
        print(self.narr[len(self.narr)//2])

m=MedianNum()
m.PrintMedian()
