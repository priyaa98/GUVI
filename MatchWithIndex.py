class MatchWithIndex:
    def __init__(self):
        self.n=int(input())
        self.narr=input()

    def Matching(self):
        self.narr=[int(i) for i in self.narr.split(" ")]
        lst=[]
        for i in range(0,self.n):
            if(self.narr[i]==i):
                lst.append(i)
        lst.sort()
        if(len(lst)==0):
            print("-1")
        else:
            for i in range(len(lst)):
                if(i==len(lst)-1):
                    print(lst[i])
                else:
                    print(lst[i],end=" ")

m=MatchWithIndex()
m.Matching()
