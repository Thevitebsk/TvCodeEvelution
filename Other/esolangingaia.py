#B8RB.py
#tried to implement the esolang "1^"

com='><=|n'
num=list(map(str,range(10)))
c="""32>|"""
p=0;s=[]
print("1^")
while True:
  if c[p]in num:s.append(int(c[p]))
  elif c[p]in com[0]:
    if s.pop()>s.pop():pass
    else:p+=1
  elif c[p]in com[3]:break
  elif c[p]in com[4]:
    while c[p]!="\n":p+=1
  elif c[p]=="\n"or len(c)<=p:
    print(c[p])
    while c[p]!="\n"or p!=0:p-=1
  print(c[p]);p+=1
print(s)
