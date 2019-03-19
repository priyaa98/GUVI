class Check:
    def __init__(self):
        self.i=int(input())
    def show(self):
        #i=int(input())
        if(self.i>0):
            print("Positive")
        elif(self.i<0):
            print("Negative")
        else:
            print("Zero")

c = Check()
c.show()
