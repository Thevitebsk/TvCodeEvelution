#-! p1 !-#
#a langauge made in python 1
c="""qHello, worldp""";p=0;s=[];ts=[];out=1
while p<len(c):
 if c[p]=="#":
  c.index("#",p+1)
 if c[p]=="q":
  s.append(c[p+1:c.index("p",p+1)])
 p=p+1
if s and out:print("".join(s))
