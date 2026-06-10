i=input("Input your code:\n").split(";");p=0
if not i[-1]:i.pop()
v={};out=""
def evalpascgolf(x):
   global p
   res=""
   if x[0]=='"':
      p+=1
      while i[p+1]!='"': res+=i[p+1]; p+=1
      p+=1; return str(res)
   elif x[0]=="v":
      try:return str(v[x[1]])
      except KeyError: print(f"No varible named \"{i[p+2]}\" exists");exit()
   else: print(f"The type \"{x[0]}\" does not exist");exit()
try:
   while p!=len(i):
      if i[p][0]=="v": v[i[p][1]]=i[p][2:]
      elif i[p][0]==".": out+=evalpascgolf(i[p][1:])
      else: print(f"not a valid pascgolf command \"{i[p][0]}\" -> pos: {p+1}");exit()
      p+=1
except IndexError:print("Program did not encounter an end statement!");exit()
print(out if out else None)
