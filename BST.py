class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data= data
        self.lh=0
        self.rh=0

    def insert_node(self,data):
        if data < self.data:
            if self.l_child== None:
                self.l_child= Node(data)
            else:
                (self.l_child).insert_node(data)
        elif data > self.data:
            if self.r_child== None:
                self.r_child= Node(data)
            else:
                (self.r_child).insert_node(data)
        else:
            self.data=data

    def printtree(self):
        if self.l_child != None:
            self.l_child.printtree()
        if self.data != None:
            print(self.data)
        if self.r_child != None:
            self.r_child.printtree()

def getHeight(root):
    if(root==None):
        return 0
    lh=getHeight(root.l_child)
    rh=getHeight(root.r_child)
    if lh>=rh:
        return lh+1
    else:
        return rh+1


root= Node(12)
root.insert_node(6)
root.insert_node(14)
root.insert_node(3)
root.insert_node(1)
root.insert_node(7)
root.insert_node(15)
root.printtree()
print(getHeight(root))
            
            
        
