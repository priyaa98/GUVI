class FindNotRepeated:
    def __init__(self):
        self.n=int(input())
        self.narr=input()

    def ToFind(self):
        arr=[int(i) for i in (self.narr).split(" ")]
        dict1={}
        l=0
        for i in arr:
            dict1[i]=0
        for i in arr:
            dict1[i]+=1
        for i in dict1:
            if(dict1[i]==1):
                l=i
                break
        print(l)        

ft=FindNotRepeated()
ft.ToFind()
    
