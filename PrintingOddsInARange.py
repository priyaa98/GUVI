class printodds:
    def __init__(self):
        self.nq=input()
        self.nq=[int(i) for i in self.nq.split(" ")]
    def printing(self):
        lst=[]
        for i in range(self.nq[0]+1,self.nq[1]):
            if(i%2!=0):
                lst.append(i)
        for i in range(0,len(lst)):
            if(lst[i]==lst[len(lst)-1]):
                print(lst[i])
            else:
                print(lst[i],end=" ")

p=printodds()
p.printing()
