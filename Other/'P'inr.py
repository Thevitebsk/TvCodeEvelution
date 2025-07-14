#TdPd.py

print("'Python' is not recognized")
c,p,s,trla=input(),0,[],""
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="?"and c[p+1]=="[":
  if s[-1]!=s[-2]:p=c.index("]",p)
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":print(c[p+1],end="");p+=1
 if c[p]=="j":
  trla=str(c[p+1]);p+=2
  while 1:
   if len(c)==p:p=0
   elif c[p]==trla and c[p-1]==":":break
   p+=1
 if c[p]=="\"":p=c.index("\"",p)
 p+=1
