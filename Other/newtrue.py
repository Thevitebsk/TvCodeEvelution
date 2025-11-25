import sys
try:
  code = open(sys.argv[1]).read()
  try: i = open(sys.argv[2]).readlines()
  except IndexError: i=[]
  except FileNotFoundError:print(f"File: {sys.argv[2]} doesn't exist");exit()
except IndexError: print(f"Usage: python {__file__.split(chr(0x5c))[-1]} \"(file name)\"");exit()
except FileNotFoundError: print(f"File: {sys.argv[1]} doesn't exist");exit()
p=0; s=[]; ld=[]
if not code:code="\n"
while 1:
  if code[p]=='"': s.append(code[p+1:code.index('"',p+1)]);p=code.index('"',p+1)
  elif code[p]==".": print(s.pop())
  elif code[p]==",":
    if i:s.append(i.pop(0))
    else:print("Input reached an EOF");exit()
  elif code[p]in"0123456789": s.append(int(code[p]))
  elif code[p]=="[": p=code.index("]", p)
  elif code[p]=="+": s.append(int(s.pop())+int(s.pop()))
  elif code[p]=="-": s.pop()
  elif code[p]=="`": s.append(int(s.pop())*-1)
  elif code[p]==":": s.append(s[-1])
  elif code[p]=='(':
    p+=1; ld.append(code[p+1:code.index(')', p)]); p=code.index(')', p)
  if code[p]=="\n":break
  if len(code)==p+1:p=-1
  p+=1
