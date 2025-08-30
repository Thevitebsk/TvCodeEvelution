#IeLe.py (snippet)

print("Pascgolf")
i=input("Input your code:\n");p=0
o=0;v={};ts=[]
try:
   while len(i)>p:
      if i[p]=="[": o+=1
      elif i[p]=="]": o-=1
      elif i[p]=="v": v[i[p+1]]=i[p+2:i.index(";",p)];p=i.index(";",p)
      elif i[p]==".":
         if i[p+1]=="\"":
            print(i[p+2:i.index("\"",p+2)]);p=i.index("\"",p+2)
         if i[p+1]=="v":
            try:print(v[i[p+2]])
            except KeyError: print(f"No varible named \"{i[p+2]}\" exists")
            p+=2
      elif i[p]not in"[]"and o==0:print("command not in brackets");exit()
      else:print(f"not a valid pascgolf command \"{i[p]}\" -> {p}");exit()
      p+=1
except IndexError:...
