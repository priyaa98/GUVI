class CamelCase:
    def __init__(self):
        self.sen=input()

    def Casing(self):
        inp_list=self.sen.split(" ")
        for i in range(len(inp_list)):
            inp_list[i]=list(inp_list[i])
        for i in range(len(inp_list)):
            for j in range(len(inp_list[i])):
                if(j==0):
                    inp_list[i][j]=inp_list[i][j].upper()
                else:
                    inp_list[i][j]=inp_list[i][j].lower()
            inp_list[i]="".join(inp_list[i])
        self.sen=" ".join(inp_list)
        print(self.sen)

c=CamelCase()
c.Casing()
