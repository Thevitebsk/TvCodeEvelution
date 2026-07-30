def is_int(x:str,pos:int=-1) -> bool:
  try:
    int(x)
    if pos==1:
      return True if int(x)>-1 else False
    elif pos==0:
      return True if int(x)<1 else False
    elif pos==-1: return True
  except: return False

def eval(x:str) -> list[str]:
  s=[[],[]];p=0
  try: return int(x)if str(float(x))[-2:]==".0"else float(x)
  except ValueError:
    if x[0]=="'":
      return x.strip("'")
    
    elif x[0]=="\"":
      p+=1
      while p!=len(x)and x[p]!="\"":
        s[0].append(x[p])
        if x[p]==","and x[p-1]!="\\":
          s[1].append("".join(s[0]))
          s[0]
        p+=1
      s[1].append("".join(s[0]))
      return s[1]

    else:return []

print("""Tally (TIB Inc.'s very own APL)
Note that this is a recreation so this could be not 1:1""")
p=1;c=""

import sys
try: c=open(sys.argv[1]).read()
except IndexError:
  while (i:=input(f"{p}:"))!="": c+= i+"\n"; p+=1
c=c.strip()
p=0;MASS=[];s=[]

while p<len(c):
  if c[p]=="{"and c[p+1]!="}": MASS.append(eval(c[p+1:c.index("}",p)]));p=c.index("}",p)
  elif c[p]=="∃": p=c.index("∄",p)
  elif c[p]=="□": MASS.append([input()])
  elif c[p]=="$":
    try:
      c[p+1]
      if is_int(c[p+1]): s.append(MASS.pop(int(c[p+1])))
      else: s.append(MASS.pop(0))
    except IndexError: s.append(MASS.pop(0))
  p+=1
for i in MASS: print(i)