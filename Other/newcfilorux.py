print("CFILORUX\n"+"-"*38)
t=[];codef=[]
from sys import argv;from time import time

# Input
stack=[]; point=n=0
try:codef=open(argv[1]).read()
except:
  while (code:=input(f"{n+1}: ")).strip()!="":codef.append(code);n+=1
try:m=int(open(argv[2]).read())
except:m=4096

# The Language
start=time();out=""
code="\n".join(codef)
la={}
def numb()->str:
  global point
  l=[]
  while point!=len(code)and code[point]in"0123456789":l.append(code[point]);point+=1
  point-=1;return int("".join(l))

n=0
while len(code)>point and n<m:
  if code[point]in"0123456789":stack.append(numb())
  elif code[point]==",":t.append(f"{time()-start:.5f}");stack.append(input());start=time()
  elif code[point]==".":out+=str(stack.pop())
  elif code[point]=='"':stack.append(code[point+1:(point:=code.index('"',point+1))])
  elif code[point]=="(":la[code[point+1:(point:=code.index(')',point+1))]]=point
  elif code[point]=="!":point=la[stack.pop()]
  point+=1;n+=1

x=time()-start;[x:=x+float(i)for i in t]
print("-"*38+"\n"+out if out else None)
print("-"*38,f"{x:.5f} seconds",sep="\n")
