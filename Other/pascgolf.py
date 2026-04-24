i=input("Input your code:\n");p=o=0;BACK=False
v={};out=""
def evalpascgolf(x):
   global p
   res=""
   if x[0]=='"':
      p+=1
      while i[p+1]!='"': res+=i[p+1]; p+=1
      p+=1; return str(res)
   elif x[0]=="v":
      try:p+=3; return str(v[x[1]])
      except KeyError: print(f"No varible named \"{i[p+2]}\" exists");exit()
   else: print(f"The type \"{x[0]}\" does not exist");exit()
try:
   while i[p]!=";"and p!=len(i)-1:
      if i[p]=="v": v[i[p+1]]=i[p+2:i.index(";",p)]; p=i.index(";",p)+1; BACK=True
      elif i[p]==".": out+=evalpascgolf(i[p+1:p+3])
      else: print(f"not a valid pascgolf command \"{i[p]}\" -> pos: {p+1}");exit()
      if not BACK:p+=1
      else:BACK=False
except IndexError:print("Program did not encounter an end statement!");exit()
print(out if out else None)
