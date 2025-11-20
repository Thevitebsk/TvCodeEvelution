A=input("English: ").lower().split(" ");B=0;C=[]
while B!=len(A):
  if A[B]=="and":C.append("i")
  elif A[B]=="hate":C.append("hrrr")
  elif A[B]in["no","not","don't","doesn't"]:C.append("hr")
  elif A[B]=="maybe":C.append("wy")
  elif A[B]in ["greet","hi","hello"]:C.append("hi")
  elif A[B]=="say":C.append("tag")
  elif A[B]=="to":C[-1]+="o"if C else""
  elif A[B]=="on":C[-1]+="a"if C else""
  elif A[B]=="active":C.append("systipu")
  elif A[B]in["me","i"]:C.append("esel")
  elif A[B]=="you":C.append("hr esel")
  elif A[B]in["he","him"]:C.append("msel")
  elif A[B]in["she","her"]:C.append("rsel")
  elif A[B]in["it","this","they","them"]:C.append("isel")
  elif A[B][0:3]=="pay"and A[B+1]=="attention":C.append("scaselet");B+=1
  elif A[B]in["here","there"]:C[-1]+="ui"if C else"";C.append("wy")
  elif A[B]=="place":C.append("iselui")
  elif A[B]=="is":
    if A[B+1]!="by":C[-1]+="h"
    else:C[-1]+="po";B+=1
  B+=1
print("   ITAC: "+" ".join(C)if C else None)
