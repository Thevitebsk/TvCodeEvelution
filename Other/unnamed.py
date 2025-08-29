stack=[];var={}
out="";code="""

""".strip()
s=tr=p=0
if code=="":s=1;out+=input()
while len(code)!=p and not s:
 if len(out)>1023:tr=1;break
 if code[p]in"0123456789":stack.append(int(code[p]))
 if code[p]=="•":var[code[p+1]]=stack.pop()
 if code[p]==",":
  try:
   if code[p+1] in var:stack.append(var[code[p+1]])
   else:out+=str(stack.pop())
  except:out+=str(stack.pop())
 p+=1
print("~"*15+" RESULT "+"~"*15)
print(out,"~"*38,"STACK: "+str(stack),"VARIABLES: "+str(var),sep="\n")
if tr:print("T")
