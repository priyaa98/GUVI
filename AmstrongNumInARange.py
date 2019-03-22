class amstrongnum:
    def __init__(self):
        self.numchar=input()
        self.numchar=[int(i) for i in (self.numchar).split(" ")]
        
    def findamstrong(self):
        countnum=0
        sumn=0
        lst=[]
        
        for num in range(self.numchar[0]+1,self.numchar[1],1):
            n=num
            countnum=len(str(n))
            sumn=0
            while(num>0):
                if(num%10>=0):
                    tmp=pow(num%10,countnum)
                    sumn=sumn+tmp
                    num=int(num/10)
            if(sumn==n):
                lst.append(n)
    
        for i in range(0,len(lst)):
            if(lst[i]==lst[len(lst)-1]):
                print(lst[i])
            else:
                print(lst[i],end=" ")
            

cd=amstrongnum()
cd.findamstrong()
