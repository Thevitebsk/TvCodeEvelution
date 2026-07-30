at=" ABCDEFGHIJKLMNOPQRSTUVWXYZ";A=B=0
for c in input(">"):
  A %= 27
  if c == "+":A += 1
  elif c == "-":A -= 1
  elif c == "'":print(at[A], end='')
  elif c == "`":A=int(input())
  elif c == "^":B=A;A=0
  elif c == "v":A=B;B=0
  else:print("X");break