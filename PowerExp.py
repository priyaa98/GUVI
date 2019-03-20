class powerexp:
    def __init__(self):
        self.nkarr=input()
        self.nkarr=(self.nkarr).split(" ")
        self.nkarr=[int(i) for i in self.nkarr]
    def calc(self):
        muln=1
        for i in range(0,self.nkarr[1]):
            muln=muln*self.nkarr[0]
        print(muln)

p= powerexp()
p.calc()
