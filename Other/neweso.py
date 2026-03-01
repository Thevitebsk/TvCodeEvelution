#6jCW.py

from os import *
dir=path.join(path.dirname(path.abspath(__file__)), "ESO")
if path.exists(dir) and path.isdir(dir):...
else:
  print("Please include an \"ESO\" folder to save your codes for further use"
      ,"Ending sesion\n",sep="\n")
  exit()

print("@@@ @@@ @@@\n"+
      "@   @   @ @\n"+
      "@@@ @@@ @ @\n"+
      "@     @ @ @\n"+
      "@@@ @@@ @@@\n"+
      "\nA collection of interpriters made by Gaham\n")

while 1:
  i=input(">>  ").upper()
  print(i.split(" ")[1::])
  if i=="END":print("Ending sesion\n");exit()
  elif i.split(" ")[0]=="START":
    try:i.split(" ")[1]
    except IndexError:print("START expected 1 argument (0 were given)")
    else:
      if i.split(" ")=="8IAL":print("Starting \"8 Instruction Assembly Language\"")
