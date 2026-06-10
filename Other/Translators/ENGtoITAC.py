A=input("English: ").lower().split(" ");B=0;C=""
while B!=len(A):
  if A[B]=="and":C+="i "
  elif A[B]=="hate":C+="hrrr "
  elif A[B]in["no","not","don't","doesn't"]:C+="hr "
  elif A[B]=="maybe":C+="wy "
  elif A[B]in ["greet","hi","hello"]:C+="hi "
  elif A[B]=="say":C+="tag "
  elif A[B]=="to":C=C[0:-1]+"o "
  elif A[B]=="on":C=C[0:-1]+"a "
  elif A[B]=="active":C+="systipu "
  elif A[B]in["me","i"]:C+="esel "
  elif A[B]=="you":C+="hr esel "
  elif A[B]in["he","him"]:C+="msel "
  elif A[B]in["she","her"]:C+="rsel "
  elif A[B]in["it","this","they","them"]:C+="isel "
  elif A[B]=="pay"and A[B+1]=="attention":C+="scaselet ";B+=1
  elif A[B]in["here","there"]:C=C[0:-1]+"ui wy "
  elif A[B]=="place":C+="iselui "
  elif A[B]=="is":
    if A[B+1]!="by":C=C[0:-1]+"h "
    else:C=C[0:-1]+"po "
    B+=1
  B+=1
print("   ITAC: "+C)
