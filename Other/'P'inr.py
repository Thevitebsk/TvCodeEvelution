#TdPd.py

print("'Python' is not recognized")
c,p,s,l=input(),0,[],{}
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="?":
  if s[-1]!=s[-2]:
    if c[p+1]=="[":p=c.index("]",p)
    elif c[p+1]=="j":p+=2
    else:p+=1
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":
    if not s:print(c[p+1],end="");p+=1
    else:print(s.pop())
 elif c[p]=="j":
  try:p=c.index(str(c[p+1]))
  except ValueError:l[c[p+1]]=p+1
 elif c[p]=="\"":p=c.index("\"",p+1)
 elif c[p]in "0123456789":s.append(int(c[p]))
 p+=1
