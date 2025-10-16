import sys;a={};b=[];c=0;d=[];e=0
for f in range(1,17):a[f]=0
try:g=open(sys.argv[1]).readlines()
except(FileNotFoundError,IndexError):exit()
for h in g:[b.append(i)for i in h.split()]
while c<len(b)and e<512:
    if b[c]=="INC":a[int(b[c+1][1],16)]=(a[int(b[c+1][1],16)]+1)%256;c+=1
    elif b[c]=="PSH":d.append(a[int(b[c+1][1],16)]);c+=1
    elif b[c]=="OUT":print(d.pop(),end=" ")
    elif b[c]=="JMP":
        i=b[c+1];c=0;j=b[0:c].count("i")
        while c<len(b):
            if b[c]==";"+i and not j:break
            c+=1
    elif b[c]=="PUT":a[int(b[c+1][1],16)]=int(input(),16)%256;c+=1
    elif b[c]=="JIR":
        if a[int(b[c+2][1],16)]==int(b[c+3]):
            i=b[c+1];c=0;j=b[0:c].count("i")
            while c<len(b):
                if b[c]==";"+i and not j:break
                c+=1
        else:c+=3
    elif b[c]=="DEC":a[int(b[c+1][1],16)]=(a[int(b[c+1][1],16)]-1)%256;c+=1
    c+=1;e+=1
print(f"\nOP:   {len(b):>14}\nACTUAL BYTESIZE:   {len(open(sys.argv[1]).read())}")
