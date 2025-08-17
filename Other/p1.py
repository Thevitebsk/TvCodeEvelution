#-! p1 !-#
#a langauge made in python 1
c="""qHello, worldp""";p=0;s=[];ts=[];out=1
while p<len(c):
 if c[p]=="#":
  while c[p]!="#":p=p+1
 if c[p]=="q":
  while c[p+1]!="p":ts.append(c[p+1]);p=p+1
  ts.reverse()
  while len(ts)>1:ts.append(ts.pop()+ts.pop())
  s.append(ts.pop())
 p=p+1
if s!=[]and out==1:print("".join(s))
