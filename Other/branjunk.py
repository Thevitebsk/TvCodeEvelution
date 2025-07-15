#jm91.py

at=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";ocm=0;osm=""
while True:
 osm="";ocm=0
 for c in input("\n>"):
  if c == "+":ocm += 1
  elif c == "-":ocm -= 1
  elif c == "'":print(at[ocm], end='')
  elif c == "`":ocm = int(input("CSVAL:"))
  elif c == "^":osm=ocm;ocm=0
  elif c == "v":ocm=osm;osm=""
  else:print("X");break
  if ocm < 0 or ocm > 25:ocm = 0
