class Multiples:
    def __init__(self):
        self.n=int(input())
    def findmul(self):
        lst=[]
        for i in range(1,6):
            lst.append((self.n)*i)
        for i in range(0,len(lst)):
            if(i==len(lst)-1):
                print(lst[i])
            else:
                print(lst[i],end=" ")

m=Multiples()
m.findmul()
