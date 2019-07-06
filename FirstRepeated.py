n=int(input())
inp=input().split()
dict={}
for i in range(0,n):
    if inp[i] not in dict:
        dict[inp[i]]=1
    else:
        dict[inp[i]]+=1
        print(inp[i])
        break
