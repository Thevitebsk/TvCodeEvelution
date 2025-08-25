#ExhZ.py

p=tv=tv2=0; s=[]; ts=[]
c="""*`,[↺(↓)"""
while len(c)>p:
 if c[p]=="*":s.append(input())
 elif c[p]=="`":
  if c[p+1]==",":s[-1]=int(s[-1])
  elif c[p+1]==".":s[-1]=float(s[-1])
  elif c[p+1]=="\"":s[-1]=str(s[-1])
 elif c[p]=="!":
  tv2=tv=s.pop()
  while tv2>1:tv2-=1;tv*=tv2
  s.append(tv)
 elif c[p]=="↑":print(s)
 elif c[p]=="↓":print(s.pop())
 elif c[p]==":":
  while c[p]!=":":p+=1
 elif c[p]=="[":
  ts.append(list(map(int,range(1,s.pop()+1))));ts[0].reverse()
  while len(ts[0]):s.append(ts[0].pop())
 elif c[p]==")":
  if s:
   while c[p]!="(":p-=1
  else:...
 elif c[p]=="↺":s.reverse()
 p+=1
