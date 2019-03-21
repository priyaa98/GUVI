class PrimeNum:
    def __init__(self):
        self.n=int(input())
    def findprime(self):
        flag=0
        if(self.n <=1):
            print("no")
        else:
            for i in range(2, self.n):
                if(self.n%i==0):
                    flag=1
            if(flag==0):
                print("yes")
            else:
                print("no")

p=PrimeNum()
p.findprime()
