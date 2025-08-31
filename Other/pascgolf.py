#IeLe.py (snippet)

print("Pascgolf")
i=input("Input your code:\n");p=o=0
v={};out=""
try:
   while 1:
      if i[p]not in"["and o==0:print("command not in brackets");exit()
      elif i[p]=="]"and p==len(i)-1: o=-1+1
      if i[p]=="[": o+=1
      elif i[p]=="]": o-=1
      elif i[p]=="v": v[i[p+1]]=i[p+2:i.index(";",p)];p=i.index(";",p)
      elif i[p]==".":
         if i[p+1]=="\"":
            out+=i[p+2:i.index("\"",p+2)]+" ";p=i.index("\"",p+2)
         if i[p+1]=="v":
            try:out+=v[i[p+2]]+" "
            except KeyError: print(f"No varible named \"{i[p+2]}\" exists")
            p+=2
      else:print(f"not a valid pascgolf command \"{i[p]}\" -> {p}");exit()
      if o==-1:break
      p+=1
except IndexError:print("Program did not encounter an end statement!");exit()
print(out)
