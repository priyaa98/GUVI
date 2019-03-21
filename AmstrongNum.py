class amstrongnum:
    def __init__(self):
        self.numchar=input()
    def findamstrong(self):
        countnum=0
        sumn=0
        num=int(self.numchar)
        while(num>0):
            if(num%10>=0):
                countnum=countnum+1
                num=int(num/10)
        num=int(self.numchar)
        while(num>0):
            if(num%10>=0):
                sumn=sumn+((num%10)**countnum)
                num=int(num/10)
        if(sumn==int(self.numchar)):
            print("yes")
        else:
            print("no")
            

cd=amstrongnum()
cd.findamstrong()
