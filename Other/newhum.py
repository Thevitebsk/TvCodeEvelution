#BMTT.py

import sys;c="";i=""
ts=[]; s1=[]; s2=[]; os=[]; s=[s1,s2]; p=m=instr=sinstr=sp=ins=ignr=0
VERSION="0.0.5"
arg=sys.argv[1:];d=0
while 1:
 try:
  if arg[0][0]!="-":arg.pop(0)
  else:break
 except:break
while arg!=[]:
 if arg[0]=="-d":d=1
 elif arg[0]=="-i":i=arg[1];arg.pop(0)
 elif arg[0]=="-w":
  if arg[1]=="file":c=open(arg[2]);c=c.read();arg.pop(0);arg.pop(0)
  elif arg[1]=="text":c=arg[2];arg.pop(0);arg.pop(0)
 elif arg[0]=="-V":print(f"{VERSION = }");ignr=1
 else:print(f"Invalid argument \"{arg[0]}\"");break
 arg.pop(0)
while p<len(c) and ignr==0:
 if c[p]=="#":break
 elif c[p]=="'":m=1;instr+=1
 elif m==1:
  while c[p]!="'":ts.append(c[p]);p+=1
  if c[p]=="'":
   ts.reverse()
   while len(ts)>1:ts.append(str(ts.pop())+str(ts.pop()))
  s[sp].append(ts[0]);ts.pop();m=0;instr+=1
 elif c[p]=="@":s[sp].reverse();print(s[sp][0],end="");s[sp].reverse();instr+=1
 elif c[p]=="!":s.pop();instr+=1
 elif c[p]=="_":
  if ins<len(i):s[sp].append(i[ins]);ins+=1;instr+=1
  else:print("\nEOI reached");break
 elif c[p]=="(":
  instr+=1
  while c[p]!=")":p+=1
 elif c[p]=="*":
  if sp==0:sp=1
  elif sp==1:sp=0
 elif c[p]=="\n":sinstr=instr
 elif c[p]=="[":s[sp].append(len(s[sp]))
 elif c[p]in list(map(str,range(10))):s[sp].append(int(c[p]))
 p+=1
 if p==len(c):
  while p>0 and c[p-1]=="\n":p-=1
  instr=sinstr
if instr!=0:sinstr=instr
if ignr==0 and c!="":print("\n",end="")
if d==1:print(f"\"{c}\" {s1} {s2} {i} {len(c)} bytes ({sinstr} instructions)")
