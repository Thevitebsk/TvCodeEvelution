def code(i,r):
    print("stacelac interpriter")
    s=[];c=[0]*4;a=0;p=0
    for cmd in i:
        if cmd=="?":print(f"debug\nstack:{s}\nacc:{a}\ncells:{c}");break
        if cmd=="a":a+=1
        if cmd=="n":a*=-1
        if cmd=="^":s.append(a)
        if cmd=="r":a=0
        if cmd=="N":
            if a>1:a=1
            elif a<0:a=0
            elif a==1:a=0
            elif a==0:a=1
        if cmd=="f":s.reverse()
        if cmd=="p":print(s[0],end="");s.pop(0)
    return f"Returned {r%128}"