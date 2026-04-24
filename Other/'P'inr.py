print("'Python' is not recognized")
c=input()
p=0;s=[];l={}
def numb()->int:
 global p;ln=[]
 while p!=len(c) and c[p]in"0123456789":
  ln.append(c[p]);p+=1
 p-=1;s.append(int("".join(ln)))
while p!=len(c):
 if c[p]=="#":
  try:l[c[p-1]]
  except KeyError:l[c[p-1]]=p
 p+=1
p=0
while len(c)>p and c[p]!=";":
 #print(c[p:],l)
 if c[p]==":":s.append(s[-1])
 elif c[p]=="?":
  if str(s.pop())!=str(s.pop()):
    if c[p+1]=="[":p=c.index("]",p)
    elif c[p+1]=="j":p+=2
    else:p+=1
 elif c[p]=="@":s.append(input())
 elif c[p]=="|":
    if not s:print(c[p+1],end=" ");p+=1
    else:print(s.pop(),end=" ")
 elif c[p]=="j":
  try:p=l[c[p+1]]
  except KeyError:print("No label found");exit()
 elif c[p]=="\"":s.append(c[p+1:c.index("\"",p+1)]);p=c.index("\"",p+1)
 elif c[p]in"0123456789":numb()
 elif c[p]=="=":s.append(s[-1])
 elif c[p]=="_":c=c[:p]+str(s.pop())+c[p+1:];p-=1
 elif c[p]in(a:=["+","-","*","/"]):
   try:s.append(eval(str(s.pop())+a[a.index(c[p])]+str(s.pop())))
   except IndexError:...
 elif c[p]=="x":s.pop()
 p+=1
