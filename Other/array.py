#xamj.py

print("Array?")
c="""[Hello\\, world!]""";p=m=0;s=[];ar=[];i=''
while p<len(c):
 if c[p]=="[" and m==0:m=1
 elif m==1:
  if c[p]=="," and c[p-1]!="\\":
   while len(s)>1:s.append(s.pop(0)+s.pop(0))
   ar.append(s.pop())
  s.append(c[p])
  if c[p]=="]":
   m=0;s.pop()
   if s[0]==",":s.pop(0)
   s.reverse()
   while len(s)>1:s.append(s.pop()+s.pop())
   print(s)
   ar.append(s.pop().replace("\\",""))
 elif c[p]=="∃": p=c.index("∄",p)
 elif c[p]=="□": ar.append(input())
 p+=1
print("\n".join(ar))
