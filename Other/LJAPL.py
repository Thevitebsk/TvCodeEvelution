print("""
L       J    A    PPPP L
L       J   A A   P  P L
L       J  AAAAA  PPPP L
LLLL JJJ  A     A P    LLLL
Literally Just A Programing Language""")
n="\n"
while True:
  ce=f"0123456789{n} abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]`|~"
  s=[];nc=0;b=[];e=0;num=[]
  out=[];inp=input(">>")
  if inp=="exit":break
  while len(inp)>nc:
    if inp[nc]=="+":s.append(int(s.pop(0))+int(s.pop(0)))
    elif inp[nc]in ce[0:10]:s.append(int(inp[nc]))
    elif inp[nc]=="a":s.append(10)
    elif inp[nc]=="|":
      while len(out)>0:print(out.pop(0),end="")
      print();break
    elif inp[nc]=="n":out.append(int(s.pop(0)))
    elif inp[nc]=="c":out.append(ce[int(s.pop(0))])
    elif inp[nc]=="*":s.append(int(s.pop(0))*int(s.pop(0)))
    elif inp[nc]=="=":s.append(s[-1])
    elif inp[nc]==";":s.append(s.pop(0))
    elif inp[nc]=="-":s.append(int(s.pop(0))-int(s.pop(0)))
    elif inp[nc]=="/":s.append(int(s.pop(0))//int(s.pop(0)))
    elif inp[nc]=="&":s.append(int(s.pop(0))*int(s.pop(0)))
    else:print("found an unknown command at",nc+1);break
    nc+=1
