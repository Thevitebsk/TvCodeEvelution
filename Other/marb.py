#1QAW.py

import sys;y=x=mv=0;debug=0
st=[];arg=sys.argv[1:];s=dd=1;out=""
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
 try:
    if debug==1:print(f"STEP {s}\n{a[y][x]} {y} {x} {a}","==================="*2,sep="\n")
    if a[y][x]=="\\":x+=1;y-=1
    elif a[y][x]=="/":x-=1;y-=1
    elif a[y][x]=="_":print(out);break
    elif a[y][x]=="=":
        y=0
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
 except IndexError:print("Your marble has escaped");exit()
