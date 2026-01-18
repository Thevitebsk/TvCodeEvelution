#x9E9.py (snippet)

print("gammascript");v={}
p=0;f=[]
while (c:=input())!='':f.append(c)
while len(f)>p:
    b=f[p].split()
    if b[0]=="set":
        if b[2]=="=":v[b[1]]=" ".join(b[3])
        elif b[2]=="++":v[b[1]]=int(v[b[1]])+1
        elif b[2]=="++":v[b[1]]=int(v[b[1]])-1
        elif b[2]=="-":v[b[1]]=int(v[b[1]])*(-1)
        elif b[3]=="ask":v[b[1]]=input()
    elif b[0]=="write":
      try:            print(v[b[1]])
      except KeyError:print(" ".join(b[1]))
    elif b[0]=="ask":input()
    elif b[0]=="#":pass
    else:print("found error at block",p+1);break
    p+=1
