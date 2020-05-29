import os
path = r'/home/kushaldulani/Finito/Dataset/Annotated/cinthol-labels-1/'


for ft in os.listdir(path):
    print(ft)
    f=open(path+ft,'r+')
    t=f.read()
    lst = t.split("\n")
    lst = list(filter(None,lst))
    for i in range(len(lst)):
        p_list = lst[i].split()
        el =p_list[0]
        if el=="6":
            p_list[0] ="1"
            lst[i] = " ".join(p_list) 
    new ="\n".join(lst) 
    f.close()
    f=open(path+ft,"w+")
    f.write(new)
    f.close()
