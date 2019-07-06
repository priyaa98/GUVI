n=int(input())
inp=[int(x) for x in input().split()]
for i in range(0,n):
	for j in range(i+1,n):
		if inp[i]+inp[j]==0:
			print(inp[i],end=" ")
			print(inp[j],end=" ")
				
