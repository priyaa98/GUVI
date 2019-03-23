from string import punctuation as p
class StringDot:
    def __init__(self):
        self.str=input()
    def AddDot(self):
        for i in range(0,len(p)):
            if(p[i]=="."):
                print(self.str+p[i])
                break

s=StringDot()
s.AddDot()
