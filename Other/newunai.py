print("CFILORUX\n"+"-"*38)
codef = []
from sys import argv;from time import time
# Arguments
try:codef=open(argv[1]).read()
except:...

# Input
stack = []; tempstack = []; point = force = 0; n = 1
if not codef:
  while (code:=input(f"{n}: ")).strip()!="":codef.append(code);n+=1
else: ...
...if codef else exit()

# The Language
start=time()
code = "\n".join(codef)
# print(code)
def numb()->str:
  global point
  listnumb=[]
  while point!=len(code)and code[point]in"0123456789":
    listnumb.append(code[point]);point+=1
  return "".join(listnumb)

while len(code)>point:
  if code[point]in"0123456789":stack.append(int(numb()))
  elif code[point]==",":stack.append(input())
  point+=1
print(stack,f"{time()-start:.5f} seconds")