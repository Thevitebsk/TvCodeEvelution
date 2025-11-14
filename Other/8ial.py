import sys;a={};b=[];c=0;d=0
for e in range(1,17):a[e]=0
try:f=open(sys.argv[1]).readlines()
except(FileNotFoundError,IndexError):print("not file was chosen")
for g in f:[b.append(i)for i in g.split()]
while b[c]!="END"and d<4096:
    if b[c]=="INC":a[int(b[c+1][1])]=(a[int(b[c+1][1])]+1)%256;c+=1
    elif b[c]=="OUT":print(a[int(b[c+1][1])],end=" ")
    elif b[c]=="JMP":
        i=b[c+1];c=0;j=b[0:c].count("i")
        while c<len(b):
            if b[c]==";"+i and not j:break
            c+=1
    elif b[c]=="PUT":a[int(b[c+1][1])]=int(input("\n"))%256;c+=1
    elif b[c]=="JIR":
        if a[int(b[c+2][1])]==int(b[c+3])%256:
            i=b[c+1];c=0;j=b[0:c].count("i")
            while c<len(b):
                if b[c]==";"+i and not j:break
                c+=1
        else:c+=3
    elif b[c]=="DEC":a[int(b[c+1][1])]=(a[int(b[c+1][1])]-1)%256;c+=1
    c+=1;d+=1
print(f"\nOP:{len(b):>18}\nACTUAL BYTESIZE:   {len(open(sys.argv[1]).read())}")
