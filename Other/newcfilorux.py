print("CFILORUX\n"+"-"*38)
t=[];c=[]
from sys import argv;from time import time

# Input
s=[]; p=n=0
try:c=[open(argv[1]).read()]
except(IndexError,FileNotFoundError):
  while (code:=input(f"{n+1}: ")).strip()!="":c.append(code);n+=1
try:m=int(open(argv[2]).read())
except IndexError:m=4096

# The Language
c=" ".join(c)
start=time();out=""
la={}
def is_int(x)->bool:
  try:int(x);return True
  except:return False
def numb()->str:
  global p
  l=[]
  while p!=len(c)and is_int(c[p]):l.append(c[p]);p+=1
  p-=1;return int("".join(l))

n=n2=o=0
while len(c)>p and n<m:
  if c[p]in"0123456789":s.append(numb())
  elif c[p]==",":t.append(f"{time()-start:.5f}");s.append(input());start=time()
  elif c[p]==".":out+=str(s.pop())
  elif c[p]=='"':s.append(c[p+1:c.index('"',p+1)]);p=c.index('"',p+1)
  elif c[p]==":":s.append(s[-1])
  p+=1;n+=1

x=time()-start;[x:=x+float(i)for i in t]
print("-"*38+"\n"+out if out else None)
print("-"*38,f"{x:.5f} seconds",sep="\n")
