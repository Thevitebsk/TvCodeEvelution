print("CFILORUX\n"+"-"*38)
t=[];codef=[]
from sys import argv;from time import time

# Input
stack=[]; point=force=n=0
try:codef=open(argv[1]).read()
except:
  while (code:=input(f"{n+1}: ")).strip()!="":codef.append(code);n+=1

# The Language
start=time()
code="\n".join(codef)
# print(code)
def numb()->str:
  global point
  l=[]
  while point!=len(code)and code[point]in"0123456789":l.append(code[point]);point+=1
  point-=1;return int("".join(l))

while len(code)>point:
  if code[point]in"0123456789":stack.append(numb())
  elif code[point]==",":t.append(f"{time()-start:.5f}");stack.append(input());start=time()
  point+=1
x=time()-start;[x:=x+float(i)for i in t]
print(stack,f"{x:.5f} seconds")
