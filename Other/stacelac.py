def code(i):
    print("stacelac interpriter")
    s=[];a=0
    for cmd in i:
        if cmd=="a":a+=1
        if cmd=="n":a*=-1
        if cmd=="^":s.append(a)
        if cmd=="N":a=int(not a)
        if cmd=="f":s.reverse()
        if cmd=="p":print(s[0],end="");s.pop(0)