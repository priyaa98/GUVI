def findfact(n):
    if n==1:
        return n
    else:
        return n*findfact(n-1)

n=int(input())
if(n<0):
    print("Negative")
elif n==0:
    print(1)
else:
    print(findfact(n))

