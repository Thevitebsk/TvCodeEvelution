def is_int(x:str) -> bool:
  #checks if the folowing argument is an int
  try:    int(x); return True
  except: return False
def is_positive(x) -> bool:
  #checks if the argument is positive
  if not is_int(x):
    raise TypeError(x,"was suposed to be an int")
  else:
    return True if int(x)>-1 else False

def eval(x:str) -> list[str]:
  s=[[],[]];p=0
  try:
    if str(float(x))[-2:]==".0":return int(x)
    else:float(x)
  except ValueError:
    if x[0]=="'":
      return x.strip("'")
    
    elif x[0]=="\"":
      p+=1
      while p!=len(x)and x[p]!="\"":
        s[0].append(x[p])
        if x[p]==","and x[p-1]!="\\":
          s[1].append("".join(s[0]))
          s[0].remove()
        p+=1
      s[1].append("".join(s[0]))

    else:...

    try:
      x[p]
      s[1].append(eval(x[p+2:]))
    except:
      return s[1]

"""print(\"""Tally (TIB Inc.'s very own APL)
Note that this is a recreation so this could be not 1:1\""")
p=1;c=""

import sys
try: c=open(sys.argv[1],encoding='utf-8').read()
except IndexError:
  while (i:=input(f"{p}:"))!="":
      c+= i+"\n"; p+=1

p=0;MASS=[];s=[]

while p<len(c):
  if c[p]=="{"and c[p+1]!="}":
    MASS.append(
      eval(
        c[p+1:c.index("}",p)]
      )
    )
    p=c.index("}",p)
  if c[p]=="∃":
    p=c.index("∄",p)
  elif c[p]=="□":
    MASS.append([input()])
  elif c[p]=="$":
    try:
      c[p+1]
      if is_int(c[p+1]): s.append(MASS.pop(int(c[p+1])))
      else: s.append(MASS.pop(0))
    except IndexError: s.append(MASS.pop(0))
  p+=1
for i in MASS: print(MASS)"""