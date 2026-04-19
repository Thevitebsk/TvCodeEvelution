import sys;regs={};ops=[];p=ne=d=0
for _ in range(0,16):regs[_]=0
try:f=open(sys.argv[1]).readlines()
except(FileNotFoundError,IndexError):
    print("no file is used or it doesn't exist")
    exit()
for _ in f:
    for _2 in _.split(): ops.append(_2)
def is_int(x:str):
    try: int("0x"+x,16); return True
    except: return False
def eval(x):
    if is_int(x):return int(x,16)%16
    else: return int(regs[int("0x"+x[1:],16)]%256)
while ops[p]!="END"and d<4096:
    if ops[p]=="INC":\
     regs[int("0x"+ops[p+1][1:],16)]=(regs[int("0x"+ops[p+1][1:],16)]+1)%256;p+=1
    elif ops[p]=="OUT":
        print(regs[int("0x"+ops[p+1][1:],16)],end=" ");p+=1;ne=1
    elif ops[p]=="JMP":
        i=ops[p+1];j=ops.count(f";{i}");p=0
        while p!=len(ops):
            if ops[p]==f";{i}":j-=1
            if j==0:break
            p+=1
        if p==len(ops):print(f"no label \"{i}\" found");break
    elif ops[p]=="PUT":\
     regs[int("0x"+ops[p+1][1:],16)]=int("0x"+input("\n"*ne),16)%256;p+=1;ne=0
    elif ops[p]=="CMJ":
        if eval(ops[p+1])==eval(ops[p+2]):
            i=ops[p+3];j=ops.count(f";{i}");p=0
            while p!=len(ops):
                if ops[p]==f";{i}":j-=1
                if j==0:break
                p+=1
            if p==len(ops): print(f"no label \"{i}\" found");break
        else:p+=3
    elif ops[p]=="DEC":\
     regs[int("0x"+ops[p+1][1:],16)]=(regs[int("0x"+ops[p+1][1:],16)]-1)%256;p+=1
    elif ops[p][0]in[";","$"]: ...
    else: print(f"undefined instruction \"{ops[p]}\"",p);break
    p+=1;d+=1
print(f"\nOP:{len(ops):>18}\nACTUAL BYTESIZE:   {len(open(sys.argv[1]).read())}")