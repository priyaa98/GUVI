class printodds:
    def __init__(self):
        self.nq=input()
        self.nq=[int(i) for i in self.nq.split(" ")]
    def printing(self):
        count=0
        if(self.nq[0]==0 or self.nq[0]==1) and (self.nq[1]==0 or self.nq[1]==1):
            return (0)
        elif(self.nq[0]==0 or self.nq[0]==1) and self.nq[1]>1:
            i=2
        else:
            i=self.nq[0]
        while i<=self.nq[1]:
            flag=0
            for j in range(2,i):
                if(i%j==0):
                    flag=1
            if flag==0:
                count+=1
            i=i+1
        return(count)

p=printodds()
print(p.printing())
