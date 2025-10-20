i=input(">>").split()
cmd=0;s=[];o=""
while 1:
        cmd+=1;print(i[0:2],o)
        if i[0]=="out":
            if i[1]=="char":  o+=chr(int(i.pop(1)))+" ";i.pop(0);i.pop(0)
            elif i[1]=="stack":  o+=str(s.pop())+" ";i.pop(0)
        elif i[0]=="note":  i.pop(0)
        elif i[0]=="push":
            if i[1]=="in":  s.append(input("input\n"));i.pop(0)
            elif i[1]=="top":  s.append(s[-1]);i.pop(0)
            else:  s.append(i[1]);i.pop(0)
        elif i[0]=="op":
            if i[1]=="plus":  s.append(int(s.pop())+int(s.pop()));i.pop(0)
            elif i[1]=="neg":  s.append(int(s.pop())*-1);i.pop(0)
            elif i[1]=="div":  s.append(int(s.pop())/int(s.pop()));i.pop(0)
        elif i[0]=="end":  print(o);break
        else:  print(f"CMD:{cmd} UNDEFINED COMMAND");break
        i.pop(0)
