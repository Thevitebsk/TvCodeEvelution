#1QAW.py

import sys;y=x=mv=wy=0
st=[];arg=sys.argv[1:];debug=s=dd=1;out=""
while arg:
 if arg[0]=="-d":debug=1
if debug:dd=16
c="""
+  
\\?_
-^[
[ .
. =
_
"""
a=c[1:-1].split("\n")
while 1:
 if debug==1:print(f"STEP {s}",f"{a[y][x]} {y} {x} {mv}","==================="*2,sep="\n")
 if a[y][x]=="\\":x+=1;y-=1
 elif a[y][x]=="/":x-=1;y-=1
 elif a[y][x]=="_":print(out);break
 elif a[y][x]=="=":
   wy,y=y,0
   while y<len(a):
    if a[y][x]=="_":break
    else:y+=1
   
 elif a[y][x]=="[":st.append(mv)
 elif a[y][x]=="+":mv+=1
 elif a[y][x]=="-":mv-=1
 elif a[y][x]=="^":
  if st.pop():x+=1;y-=1
  else:x-=1;y-=1
 elif a[y][x]=="?":st.append(int(input()))
 elif a[y][x]==".":out+=str(st.pop())
 if s==4096//dd:print(out);break
 y+=1;s+=1
 if y>len(a)-1:print("Your marble has escaped");break
