#TdPd.py

print("'Python' is not recognized")
c=input();tp=p=cb=0;s=[];l1={};l2=[]
def numb()->int:
  global p;ln=[]
  while p!=len(c)and c[p]in"0123456789":ln.append(c[p]);p+=1
  p-=1;s.append(int("".join(ln)))
while len(c)>p:
 if c[p]==";":break
 elif c[p]==":":s.append(c[p+1]);p+=1
 elif c[p]=="?":
  if str(s.pop())!=str(s.pop()):
    s.append(0)
    if c[p+1]=="[":p=c.index("]",p)
    elif c[p+1]=="j":p+=2
    else:p+=1
  else:s.append(1)
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":
    if not s:print(c[p+1],end="");p+=1
    else:print(s.pop(),end="")
 elif c[p]=="j":
  try:p=c.index(str(c[p+1]))
  except ValueError:l1[c[p+1]]=p+1
 elif c[p]=="\"":p=c.index("\"",p+1)
 elif c[p]in"0123456789":numb()
 elif c[p]=="{":
  cb+1;tp=p
  while 1:
    if c[p]=="}":
      if not cb:l2.append([tp+1,c.index("}",p)+1]);break
      else:cb-=1
    p+=1
 elif c[p]==">":s.append(c[(x:=l2.pop())[0]:x[1]])
 elif c[p]=="=":s.append(s[-1])
 p+=1
