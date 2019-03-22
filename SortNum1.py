def PrintSorted(): 
    n=int(input())
    narr=input()
    narr=[int(i) for i in narr.split(" ")]
    narr.sort()
    for i in range(0,len(narr)):
        if(i==len(narr)-1):
            print(narr[i])
        else:
            print(narr[i],end=" ")

PrintSorted()
