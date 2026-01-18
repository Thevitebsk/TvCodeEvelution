import sys;regs={};ops=[];p=d=ne=0
for _ in range(1,17):regs[_]=0
try:f=open(sys.argv[1]).readlines()
except(FileNotFoundError,IndexError):print("no file was chosen");exit()
for _ in f:[ops.append(_2)for _2 in _.split()]
def is_int(x:str):
    try:int(x);return True
    except:return False
def eval(x):return int(x,16)%16 if is_int(x)else int(regs[int(x[1:])]%256)
while ops[p]!="END"and d<4096:
    if ops[p]=="INC":regs[int(ops[p+1][1:])]=(regs[int(ops[p+1][1:])]+1)%256;p+=1
    elif ops[p]=="OUT":print(regs[int(ops[p+1][1:])],end=" ");p+=1;ne=1
    elif ops[p]=="JMP":
        i=ops[p+1];p=0;j=ops[0:p].count("i")
        while p!=len(ops):
            if ops[p]==";"+i and not j:break
            p+=1
        print(f"no label \"{i}\" found");break
    elif ops[p]=="PUT":regs[int(ops[p+1][1:])]=int(input("\n"*ne))%256;p+=1;ne=0
    elif ops[p]=="JIR":
        if eval(ops[p+2])==eval(ops[p+3]):
            i=ops[p+1];p=0;j=ops[0:p].count("i")
            while p!=len(ops):
                if ops[p]==";"+i and not j:break
                p+=1
            print(f"no label \"{i}\" found");break
        else:p+=3
    elif ops[p]=="DEC":regs[int(ops[p+1][1:])]=(regs[int(ops[p+1][1:])]-1)%256;p+=1
    elif ops[p][0]in[";","$"]:...
    else:print(f"undefined instruction \"{ops[p]}\"",p);break
    p+=1;d+=1
print(f"\nOP:{len(ops):>18}\nACTUAL BYTESIZE:   {len(open(sys.argv[1]).read())}")
