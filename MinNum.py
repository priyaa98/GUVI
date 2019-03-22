class MinNum:
    def __init__(self):
        self.n=int(input())
        self.narr=input()
        self.narr=[int(i) for i in (self.narr).split(" ")]

    def FindMin(self):
        (self.narr).sort()
        print((self.narr)[0])

m=MinNum()
m.FindMin()

