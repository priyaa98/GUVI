class FindDiff:
    def __init__(self):
        self.str=input()
        self.str=self.str.split(" ")
    def finding(self):
        count=0
        for i in range(len(self.str[0])):
            if(self.str[0][i]!=self.str[1][i]):
                count+=1
        if(count==1):
            print("yes")
        else:
            print("no")

fd=FindDiff()
fd.finding()
