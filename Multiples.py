class Multiples:
    def __init__(self):
        self.n=int(input())
    def findmul(self):
        lst=[]
        for i in range(1,6):
            lst.append((self.n)*i)
        for i in lst:
            if(i==lst[len(lst)-1]):
                print(i)
            else:
                print(i,end=" ")

m=Multiples()
m.findmul()
