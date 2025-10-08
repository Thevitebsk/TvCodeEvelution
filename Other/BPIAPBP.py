# BPINPBC Program Isn't A Valid Python ByteCode Program
INST = {
    "0":"NOP",
    "1":"PUSH",
    "2":"ADD",
    "3":"SUB",
    "4":"MUL",
    "5":"DIV",
    "6":"JIC",
    "7":"LJP",
    "e":"OUT",
    "f":"HALT"}
import sys,time
opcodes=[];p=debug=0;n=[];tn=[];l={};time1=time.time()
print("BPINPBC Programs Aren't A Valid Python ByteCode Program")
try:sys.argv[2]
except IndexError:...
else:
    a=sys.argv[2::]
    while len(a)>0:
        if a[0] in ["-d","--debug"]: debug=1
        a.pop(0)
try:code=open(sys.argv[1]).read()
except IndexError:
    raise FileNotFoundError("No file was given")
except FileNotFoundError:
    raise FileNotFoundError(f"File {sys.argv[1]} doesn't exist")
for i in code:
    opcodes.append(hex(ord(i))[2])
    try:opcodes.append(hex(ord(i))[3])
    except IndexError:opcodes.append(0)
while opcodes[-1]=="f":opcodes.pop()
opcodes.append("f")
while p!=len(opcodes):exec("l[opcodes[p+1]]=p")if opcodes[p]=="7"else...;p+=1
p=0;print(opcodes,l)
while p!=len(opcodes):
    if time1-time.time()<-30.0:break
    try:INST[opcodes[p]]
    except KeyError:print(f"SYSTEM ERROR: INVALID OP CODE {opcodes[p]}"); break
    if opcodes[p]=="f": break
    elif opcodes[p]=="1": n.append(opcodes[p+1]); p+=1
    elif opcodes[p]=="2": n.append(n.pop()+n.pop())
    elif opcodes[p]=="3": n.append(n.pop()-n.pop())
    elif opcodes[p]=="4": n.append(n.pop()*n.pop())
    elif opcodes[p]=="5": n.append(n.pop()/n.pop())
    elif opcodes[p]=="6":
        tn.append([n[-1]<n[-2],n[-1]==n[-2],n[-1]>n[-2]])
        if opcodes[p+1]=="1"and tn[0][0]: p=l.get(p+2,0)
        elif opcodes[p+1]=="2"and tn[0][1]: p=l.get(p+2,0)
        elif opcodes[p+1]=="3"and tn[0][2]: p=l.get(p+2,0)
        tn.clear()
    p+=1
if debug:
    print(n)
    print("N:      HEX:    OPCODE:")
    for i, opcode in enumerate(opcodes):
        print(f"{i + 1:<7} {str(opcode)[0]:<8}", end="")
        try:print(INST[opcode])
        except KeyError:
            if opcode[len(opcode)-3::]!="val":print("NOP")
            else:print(f"{"ARGUMENT":<8}")
        p+=1
    print("Glyphs:\n"+code)
