i="""""";p=-1;tp=po=sub=0;targ="";c=""
ts=[];s=[]
print("true")
while 1:
 try:
  p+=1
  if i[p]=='"': s.append(i[p+1:i.index("\"",p+1)]); p=i.index("\"",p+1)
  elif i[p]=='.': print(s.pop(),end="")
  elif i[p]in"0123456789":s.append(int(i[p]))
  elif i[p]==',':c=input()
  elif i[p]==':':s.append(s[-1])
  elif i[p]=="'":s.append(c[0]);c=c[1:len(c)]
  elif i[p]=='»':
   targ=i[p+1];tp=p;sub=1
   while 1:
    if i[p]==targ and i[p+1]==":":p+=1;break
    if len(i)-2==p:p=0
    p+=1
  elif i[p]==";"and sub==1:p=tp
  elif i[p]=="\n":break
 except IndexError:break
