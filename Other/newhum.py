#BMTT.py

import sys;c="";i=[]
s1=[]; s2=[]; os=[]; s=[s1,s2]; p=sp=ins=0
VERSION="0.0.6"
arg=sys.argv[1:];d=0
while len(arg):
 if arg[0]=="-d":d=1
 elif arg[0]=="-i": i=open(arg.pop(1)).readlines()
 elif arg[0]=="-w": c=open(arg.pop(1)).read()
 elif arg[0]=="-V":print(f"V = {VERSION}");exit()
 else:print(f"Invalid argument \"{arg[0]}\"");exit()
 try:arg.pop(0)
 except IndexError:...
while 1:
 if c[p]=="#":break
 elif c[p]=="'":s[sp].append(c[p:c.index("'",p+1)])
 elif c[p]=="@":print(s[sp][-1],end="")
 elif c[p]=="!":s.pop()
 elif c[p]=="_":
  if ins!=len(i):s[sp].append(i[ins]);ins+=1
  else:print("\nEOF reached");exit()
 elif c[p]==")":
  if s[sp][-1]:
    while c[p]!="(":p-=1
 elif c[p]=="*":sp=int(not sp)
 elif c[p]=="[":s[sp].append(len(s[sp]))
 elif c[p]in"0123456789":s[sp].append(int(c[p]))
 p+=1
 if p==len(c):
  while p>0 or c[p]!="\n":p-=1
if c!="":print()
if d!=0:print(f"\"{c}\" {s1} {s2} {i} {len(c)} bytes")
