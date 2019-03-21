class printodds:
    def __init__(self):
        self.nq=input()
        self.nq=[int(i) for i in self.nq.split(" ")]
    def printing(self):
        lst=[]
        i=self.nq[0]+1
        while i<self.nq[1]:
            flag=0
            for j in range(2,i):
                if(i%j==0):
                    flag=1
            if flag==0:
                lst.append(i)
            i=i+1
        for i in range(0,len(lst)):
            if(lst[i]==lst[len(lst)-1]):
                print(lst[i])
            else:
                print(lst[i],end=" ")

p=printodds()
p.printing()

