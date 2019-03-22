class TimeDiff:
    def __init__(self):
        self.arr=input()
        self.arr2=input()
        self.arr=[int(i) for i in self.arr.split(" ")]
        self.arr2=[int(i) for i in self.arr2.split(" ")]

    def DiffCalc(self):
        t1=(60*self.arr[0])+self.arr[1]
        t2=(60*self.arr2[0])+self.arr2[1]
        diff=abs(t2-t1)
        if(diff<60):
            print("0",end=" ")
            print(diff)
        else:
            print(diff//60,end=" ")
            print(diff-((diff//60)*60))

td=TimeDiff()
td.DiffCalc()
