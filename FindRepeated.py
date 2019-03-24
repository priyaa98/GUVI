class FindRepeated:
    def __init__(self):
        self.n=int(input())
        self.narr=input()

    def ToFind(self):
        narr=[int(i) for i in self.narr.split(" ")]
        dict1={}
        lst=[]
        for i in narr:
            dict1[i]=0
        for i in narr:
            dict1[i]+=1
        for i in dict1:
            if(dict1[i]>1):
                lst.append(i)
        lst.sort()
        if(len(lst)==0):
            print("unique")
        else:
            for i in range(len(lst)):
                if(i==len(lst)-1):
                    print(lst[i])
                else:
                    print(lst[i],end=" ")

fr=FindRepeated()
fr.ToFind()
    
