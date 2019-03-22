class CheckNum:
    def __init__(self):
        self.n=input()
    def checking(self):
        flag=0
        c=0
        for i in self.n:
            if(i.isdigit()):
                continue
            elif(i=='.'):
                c=c+1
                if(c==1):
                    continue
                else:
                    flag=1
                    break
            else:
                flag=1
                break
        if (flag==0):
            print("Yes")
        else:
            print("No")

c=CheckNum()
c.checking()
            
