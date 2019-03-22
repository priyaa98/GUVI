class ArithProgression:
    def __init__(self):
        self.nadarr=input()
        self.nadarr=[int(i) for i in (self.nadarr).split()]

    def sumAP(self):
        a=self.nadarr[1]
        d=self.nadarr[2]
        n=self.nadarr[0]
        ap=0
        sumn=0
        for i in range(0,n):
            ap=a+(i*d)
            sumn=sumn+ap
        print(sumn)

AP=ArithProgression()
AP.sumAP()            
