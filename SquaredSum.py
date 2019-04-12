class SquaredSum:
    def __init__(self):
        self.n=int(input())
    def summing(self):
        s=0
        for i in range(len(str(self.n))):
            i=self.n%10
            s=s+(i*i)
            self.n=self.n//10
        print(s)

s=SquaredSum()
s.summing()
