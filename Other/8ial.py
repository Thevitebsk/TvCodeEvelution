import sys;a={};b=[];c=d=k=0
for e in range(1,17):a[e]=0
try:f=open(sys.argv[1]).readlines()
except(FileNotFoundError,IndexError):print("no file was chosen");exit()
for g in f:[b.append(i)for i in g.split()]
def h(x:str):
    try:int(x);return True
    except:return False
while b[c]!="END"and d<4096:
    if b[c]=="INC":a[int(b[c+1][1:])]=(a[int(b[c+1][1:])]+1)%256;c+=1
    elif b[c]=="OUT":print(a[int(b[c+1][1:])],end=" ");c+=1;k=1
    elif b[c]=="JMP":
        i=b[c+1];c=0;j=b[0:c].count("i")
        while c!=len(b):
            if b[c]==";"+i and not j:break
            c+=1
        else:print(f"no label \"{i}\" found",c);break
    elif b[c]=="PUT":a[int(b[c+1][1:])]=int(input("\n"*k))%256;c+=1;k=0
    elif b[c]=="JIR":
        if a[int(b[c+2][1:])]==(int(b[c+3])if h(b[c+3])else a[int(b[c+3][1:])])%256:
            i=b[c+1];c=0;j=b[0:c].count("i")
            while c!=len(b):
                if b[c]==";"+i and not j:break
                c+=1
            else:print(f"no label \"{i}\" found",c);break
        else:c+=3
    elif b[c]=="DEC":a[int(b[c+1][1:])]=(a[int(b[c+1][1:])]-1)%256;c+=1
    elif b[c][0]in[";","$"]:...
    else:print(f"undefined instruction \"{b[c]}\"",c);break
    c+=1;d+=1
print(f"\nOP:{len(b):>18}\nACTUAL BYTESIZE:   {len(open(sys.argv[1]).read())}")
