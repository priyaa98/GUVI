class primenum:
    def __init__(self):
        self.N=int(input())
    def checkprime(self):
        if(self.N>5):
            if((self.N%2==0) or (self.N%3==0) or (self.N%5==0)):
                print("no")
            else:
                print("yes")
        elif(self.N==2 or self.N==3 or self.N==5):
                print("yes")
        else:
            print("no")

pn=primenum()
pn.checkprime()
