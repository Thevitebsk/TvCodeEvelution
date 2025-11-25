"""This esolang was made by me during my IT lesson becuase i didn't want to make a \"very complicated project\""""
def code(i,u):
    s1=[];s2=[];os=[];sp=p=0;inp=[];ss=[s1,s2]
    for t in u:
        inp.append(t)
    while p!=len(i):
        if i[p]=="`":s2.append(i[p+1:i.index("`",p+1)]);p=i.index("`",p+1)
        elif i[p]=="@":os.append(s1.pop())
        elif i[p]==">":s1.append("".join(s2))
        elif i[p]=="!":ss[sp].pop()
        elif i[p]=="R":ss[sp].reverse()
        elif i[p]=="M":sp=int(not sp)
        elif i[p]=="|":p=i.index("|",p)
        elif i[p]=="_":s1.append(inp.pop(0))
        else:print("undefined command");break
        p+=1
    print(f"code:   {i}\ninput:  {u}\noutput: {"".join(os[0])}")
code("`Hello world`>@","input")
