class arraysum:
    def __init__(self):
        self.nkarr=input()
        self.nkarr=(self.nkarr).split(" ")
        self.nkarr=[int(i) for i in self.nkarr]
        self.arr=input()
        self.arr=(self.arr).split(" ")
        self.arr=[int(i) for i in self.arr]
    def sumit(self):
        sumn=0
        for i in range(0,self.nkarr[1]):
            sumn=sumn+self.arr[i]
        print(sumn)

a=arraysum()
a.sumit()
