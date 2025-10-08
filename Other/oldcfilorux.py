# --UNAI-- #
import sys
try:c=open(sys.argv[1]).read()
except:print(f"Usage: python {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
s=[];ts=[];p=io=0
def push_int():
    global p
    while 1:
     if p+1>len(c):break
     ts.append(c[p]);p+=1
     if c[p]not in"0123456789":p-=1;break
    while ts[0]=="0":ts.pop(0)
    s.append("".join(ts));ts.clear()
while len(c)>p:
    if c[p]in"0123456789":push_int()
    elif c[p]==".":print(s.pop());io=1
    elif c[p]=="\"":
        p+=1
        while c[p]!="\"":ts.append(c[p]);p+=1
        s.append("".join(ts));ts.clear()
    elif c[p]=="^":s.pop()
    elif c[p]==",":s.append(input())
    elif c[p]=="]":p=c.index("\n",p)
    p+=1
if io==0:print("\n".join(s))
