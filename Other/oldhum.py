"""This esolang was made by Gaham (User:Ractangle) during his IT lesson becuase he didn't want to make a very complicated project (A.K.A. Making a sims game in python)
`...` pushes every symbol surrounded by ` to string stack
> move all the elements on the string stack to the stack
@ prints the top value on the stack
# starts program. stops program if encounterd again.
! Pops the top value on the (string) stack
R Flips the (string) stack
M Changes the stack pointers position
|...| Comment
_ input"""
m="";s=[];ss=[];os=[];sp=0;inp=[]
def code(i,u):
    global m,sp
    for t in u:
        inp.append(t)
    for c in i:
        if m=="e":break
        elif c=="`" and m=="c":m="s"
        elif c=="`" and m=="s":m="c"
        elif m=="s":ss.append(c)
        elif c=="@" and m=="c":s.reverse();os.append(s[0]);s.reverse();s.pop()
        elif c==">" and m=="c":
            while len(ss)>1:a=str(ss[0])+str(ss[1]);ss.pop(0);ss.pop(0);ss.reverse();ss.append(a);ss.reverse()
            while len(ss)>0:s.append(ss[0]);ss.pop(0)
        elif c=="#":m="c"
        elif c=="!" and sp==0:ss.pop()
        elif c=="!" and sp==1:s.pop()
        elif c=="R" and sp==0:ss.reverse()
        elif c=="R" and sp==1:s.reverse()
        elif c=="M" and sp==0:sp=1
        elif c=="M" and sp==1:sp=0
        elif c=="|":m=="no"
        elif c=="|" and m=="no":m==c
        elif c=="_" and m=="c":s.append(inp[0]);inp.pop(0)
        else:print("undefined command");break
    print(f"code:\n{i}\nstring stack:\n{ss}\nstack:\n{s}\ninput:\n{u}\noutput:")
    while len(os)>0:print(os[0]);os.pop(0)
code("#`Hello world`>@","input")
