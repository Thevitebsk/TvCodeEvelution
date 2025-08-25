#x9E9.py (snippet)

print("gammascript");v={};f={}
p=0;c=' ';cs=[];fs=[];sp=0
while c!='':c=input();cs.append(c)
cs.pop()
while len(cs)>p:
    b=cs[p].split()
    if b[0]=="set":
        if b[2]=="=":v[b[1]]=" ".join(b[3:])
        elif b[2]=="++":v[b[1]]=int(v[b[1]])+1
        elif b[2]=="-":v[b[1]]=int(v[b[1]])*(-1)
        elif b[3]=="ask":v[b[1]]=input()
    elif b[0]=="show":print(v[b[1]])
    elif b[0]=="write":print(" ".join(b[1:]))
    elif b[0]=="ask":input()
    elif b[0]=="#":pass
    else:print("found error at block",p+1):break
    p+=1
