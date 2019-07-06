nm=input()
nm=[int(x) for x in nm.split()]
n=nm[0]
m=nm[1]
flag=0
n_list=input()
m_list=input()
for i in m_list:
    if i not in n_list:
        flag=1

if flag==1:
    print("NO")
else:
    print("YES")
