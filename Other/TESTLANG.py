i=input(">>").split()
cmd=0;s=[];inp='';o=[]
while len(i)!=0:
        cmd+=1
        if i[0]=="out":
            if i[1]=="char":
                o.append(chr(int(i.pop(1))))
                i.pop(0);i.pop(0)
            else:
                o.append(i.pop(1));i.pop(0)
        elif c[0]=="note":c.pop(0);c.pop(0)
        elif c[0]=="in":inp=input("input\n");c.pop(0)
        elif c[0]=="push":
            if c[1]=="in":
                s.append(inp)
                c.pop(0);c.pop(0)
            elif c[1]=="out":
                o.append(s.pop(0))
                c.pop(0);c.pop(0)
            else:
                s.append(c[1])
                c.pop(0);c.pop(0)
        elif c[0]=="op":
            if c[1]=="plus":
                r=int(s[0])+int(s[1])
                s.append(int(s.pop(0))+int(s.pop(0)))
                c.pop(0);c.pop(0)
        elif c[0]=="end":print("".join(str(o)));break
        else:print(f"CMD:{cmd} UNDEFINED COMMAND");break
