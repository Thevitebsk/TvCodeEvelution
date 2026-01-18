#shut up it counts as a translator to me

mm=input("MM:").split(" ");p=x=0;r={}
def MM(x:int)->str:
  a=["0","1","2","3","4","5","6","7","8","9",
     "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",
     "Q","R","S","T","U","V","W","X","Y","Z"]
  return (str(a[x%(F:=36)])+str(a[x//F%F])+str(a[x//F//F%F])+str(a[x//F//F//F%F]))[::-1]
while len(mm)>p:
  print(f";{MM(x)}",end=" ")
  if mm[p][0]=="0":   print(f"INC ${int(mm[p][1:])}",end=" ");x+=1
  elif mm[p][0]=="1":
    try:             r[int(mm[p][1:])%16]
    except KeyError: r[int(mm[p][1:])%16]=0
    print(f"JIR {MM(r[int(mm[p][1:])%16])} ${int(mm[p][1:])} 0 DEC ${int(mm[p][1:])}",end=" ")
  p+=1;x+=1
print("END")
