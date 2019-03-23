class RomNum:
    def __init__(self):
        self.rom={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M':1000}
        self.inp=input()

    def findNum(self):
        num=0
        for i in range(len(self.inp)):
            if(i==len(self.inp)-1):
                num=num+self.rom[self.inp[i]]
            else:
                if(self.rom[self.inp[i+1]]<=self.rom[self.inp[i]]):
                    num=num+self.rom[self.inp[i]]
                else:
                    num=num-self.rom[self.inp[i]]
        print(num)

r=RomNum()
r.findNum()
