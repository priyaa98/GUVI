class RemVowels:
    def __init__(self):
        self.n=int(input())
        self.inp=input()
    def removing(self):
        inp=list(self.inp)
        vowels=['a','e','i','o','u','A','E','I','O','U']
        for j in range(self.n):
            for i in inp:
                if i in vowels:
                    inp.remove(i)
        inp=inp[::-1]
        inp=''.join(inp)
        print(inp)

rv=RemVowels()
rv.removing()
