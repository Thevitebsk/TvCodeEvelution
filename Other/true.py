import sys
try:
  code = open(sys.argv[1]).read()
  try: i = open(sys.argv[2]).readlines()
  except: i=[]
except: print(f"Usage: python {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
p = tp = 0; ts = []; s = []; ld = []; tcode = ""
if not code : code = " "
while 1:
  if code[p] == '"' :
    p+=1; s.append(code[p : code.index('"', p)])
    p=code.index('"', p)
  elif code[p] == "." : print(s.pop())
  elif code[p] == "," : 
    if i : s.append(i.pop(0))
    else : raise EOFError("Input reached an EOF")
  elif code[p] in "0123456789" : s.append(int(code[p]))
  elif code[p] == "[" : p=code.index("]", p)
  elif code[p] == "+" : s.append(int(s.pop())+int(s.pop()))
  elif code[p] == "-" : s.pop()
  elif code[p] == "`" : s.append(int(s.pop())*-1)
  elif code[p] == ":" : s.append(s[-1])
  elif code[p] == '(' :
    p+=1; ld.append(code[p : code.index(')', p)]+")")
    p=code.index(')', p)
  if code[p] == "\n" : break
  if len(code) == p +1 : p = -1
  p += 1
