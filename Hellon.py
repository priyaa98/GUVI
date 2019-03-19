class Hello:
    def __init__(self):
        self.n= int(input())
    def printing(self):
        for i in range(0,self.n):
            print("Hello")

h= Hello()
h.printing()
