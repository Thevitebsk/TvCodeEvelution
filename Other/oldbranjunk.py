for c in input(">"):
  A %= 27
  if c == "+":A += 1
  elif c == "-":A -= 1
  elif c == "U":print(chr(A), end='')
  elif c == "K":break
  elif c == ";":A=int(input())
  elif c == ":":A=0
  else:print("X");break