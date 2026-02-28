#j7Vl.py

import os
print("@@@ @@@ @@@\n"+
      "@   @   @ @\n"+
      "@@@ @@@ @ @\n"+
      "@     @ @ @\n"+
      "@@@ @@@ @@@\n"+
      "\nA collection of interpriters made by Gaham\n")

try: open("/".join(os.path.dirname(os.path.abspath(__file__)).split(chr(0x5c))[0::])+"/ESO")
except: print("Please include an \"ESO\" folder for storing information after your ESO sesion");exit()

while 1:
  i=input(">>  ").upper()
  if i=="END":print("Ending sesion\n");exit()
  elif i=="GAL":print("Launching \"Gatari's Assembly Language\"")
