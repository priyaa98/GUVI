class sumnat:
    def __init__(self):
        self.n=int(input())
    def sumnum(self):
        sumn=0
        for i in range(1,(self.n)+1):
            sumn=sumn+i
        print(sumn)

s=sumnat()
s.sumnum()

