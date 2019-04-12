class findmaxrep:
    def __init__(self):
        self.inp=input()
    def finding(self):
        dict1={}
        for i in self.inp:
            dict1[i]=0
        for i in self.inp:
            dict1[i]+=1
        if " " in dict1:
            del dict1[" "]
        for i in dict1:
            if(dict1[i]==max(dict1.values())):
                print(i)

fmr=findmaxrep()
fmr.finding()
