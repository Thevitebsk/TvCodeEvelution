import sys
try:
  code = open(sys.argv[1]).read()+" "
  try: i = open(sys.argv[2]).readlines()
  except IndexError: i=[]
  except FileNotFoundError:print(f"File: {sys.argv[2]} doesn't exist");exit()
except IndexError: print(f"Usage: python {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
except FileNotFoundError: print(f"File: {sys.argv[1]} doesn't exist");exit()
p=tp=0; s=[]; ts=[]
if not code:code="\n"
while 1:
  if code[p]=='"': s.append(code[p+1:code.index('"',p+1)]);p=code.index('"',p+1)
  elif code[p]==".": print(s.pop(),end=" ")
  elif code[p]==",":
    if i:s.append(i.pop(0))
    else:print(f"Input reached an EOF, to add input do: python {__file__.split(chr(0x5c))[-1]} \"(file name)\" \"(file name for input)\"");exit()
  elif code[p]in"0123456789": s.append(int(code[p]))
  elif code[p]=="[": p=code.index("]", p)
  elif code[p]=="+": s.append(int(s.pop())+int(s.pop()))
  elif code[p]=="*": s.append(int(s.pop())*int(s.pop()))
  elif code[p]=="//": s.append(int(s.pop())//int(s.pop()))
  elif code[p]=="-": s.pop()
  elif code[p]=="`": s.append(int(s.pop())*-1)
  elif code[p]==":": s.append(s[-1])
  elif code[p]=='(':
    s.append(code[p:(p:=code.index(')', p))])
  elif code[p]=="?":
    if s:
     ts.append(s.pop());ts.append(s.pop())
     while tp<len(ts[-1]):
         if ts[-1][tp]in"0123456789": s.append(int(ts[-1][tp]))
         elif ts[-1][tp]==">":CR="T"if s.pop()>s.pop()else"F"
         elif ts[-1][tp]=="=":CR="T"if s.pop()==s.pop()else"F"
         elif ts[-1][tp]=="<":CR="T"if s.pop()<s.pop()else"F"
         tp+=1
     if CR=="T":p+=2;code=code[:p]+ts.pop(0)+code[p+1:];CR="";ts.clear()
     else:p+=1;CR="";ts.clear()
  elif code[p]=="|":break
  if len(code)==p+1:
   if "\n"not in code:p=-1
   else:p=len(code)-code[::-1].index("\n")
  p+=1
