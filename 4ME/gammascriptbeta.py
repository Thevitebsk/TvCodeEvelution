#v9ku.py
#take two of the the alpha version

i="""
create var x, 1
if x is 1 then:
write x
""".strip()
print("gammascript v0.2");p=0
v = {};kw=[j.split(" ")for j in i.split("\n")]
while p!=len(kw):
  for x in kw:
    if ' '.join(x[0:2])=="create var"and x[2][-1]==",": v[x[2][0:-1]] = ' '.join(x[3:])
    elif x[0]=="write":print(" ".join(x[1:])[1:-1]if x[1][0]=='"'else v[x[1]])
    elif x[0]=="if"and x[2]=="is"and x[4]=="then:":
      print("PLACEHOLDER")
    p+=1
