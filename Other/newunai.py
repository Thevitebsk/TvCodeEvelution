# UNAI #
codef = []; uin = []
import sys,time
# Arguments
try:codef=open(sys.argv[1]).read()
except:...
else:
  try:uin=open(sys.argv[2]).readlines()
  except:...

# Input
stack = []; tempstack = []; point = force = 0; n = 1
if not codef:
  while 1:
    code=input(f"{n}: ")
    if code.strip() != "" : codef.append(code)
    else: break
    n+=1
else: ...
... if codef else exit()

# The Language
starttime=time.time()
code = "\n".join(codef)
# print(code)
def numb()->str:
  global point
  listnumb=[]
  while point!=len(code)and code[point]in"0123456789":
    listnumb.append(code[point])
    point+=1
  return "".join(listnumb)

while len(code)>point:
  print(code[point])
  if code[point]in"0123456789":stack.append(int(numb()))
  elif code[point]==",":stack.append(input())
  point+=1
print(stack,f"{time.time()-starttime:.3f} seconds")
