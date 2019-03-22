class fact:
    def __init__(self):
        self.n=int(input())
    def findfact(self):
        if(self.n==1 or self.n==0):
            fact=1
        else:
            fact=1
            for i in range(self.n,0,-1):
                fact=fact*i
        print(fact)

f=fact()
f.findfact()
