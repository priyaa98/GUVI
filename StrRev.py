class StrRev:
    def __init__(self):
        self.n=input()

    def Rev(self):
        self.n=self.n[::-1]
        print(self.n)

s=StrRev()
s.Rev()
