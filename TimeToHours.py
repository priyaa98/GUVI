class TimeToHours:
    def __init__(self):
        self.n=int(input())
    def Convert(self):
        if(self.n<60):
            print("0", end=" ")
            print(self.n)
        else:
            print(self.n//60,end=" ")
            print(self.n-((self.n//60)*60))

th=TimeToHours()
th.Convert()
