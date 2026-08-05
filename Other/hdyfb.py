debug=0
claw=cp=dp=0;tape=[0]*8
code="""II=+=+=+=+=^↑v=+^II=+=+v+P=^^↓v+DDDP^I=+=+=+Dv+PPIIIP^II=+=+=+=+PvvIIIIIIIIIIIIIIIP^PIIIPDDDDDDP^^DD+=+=+vv↑^^^↓v+PvIPH""".strip()
while cp!=len(code):
  if code[cp]=="I":tape[dp]+=1
  elif code[cp]=="D":tape[dp]-=1
  elif code[cp]=="^":dp+=1
  elif code[cp]=="v":dp-=1
  elif code[cp]=="P":print(chr(tape[dp]),end="")
  elif code[cp]=="N":print(tape[dp],end=" ")
  elif code[cp]=="=":tape[dp+1]=tape[dp]
  elif code[cp]=="+":tape[dp]=tape[dp+1]+tape[dp];tape[dp+1]=0
  elif code[cp]==")":
    if tape[dp]!=0:
      while code[cp]not in"\n|": cp-=1
  elif code[cp]=="/": cp+=1 if tape[dp]!=0 else 0
  elif code[cp]=="↑":
    if claw!=0:print("claw aready defined");exit()
    claw=tape[dp];tape[dp]=0
  elif code[cp]=="↓":
    if claw==0:print("claw undefined");exit()
    tape[dp]=claw;claw=0
  elif code[cp]=="H": break
  elif code[cp]=="G": cp=tape[dp]if tape[dp]>0 else cp
  elif code[cp]==";":
      try:tape[dp]=int(input())
      except EOFError:print("EOF reached");exit()
      except ValueError:print("int expected")
  elif code[cp:cp+2]=="->":
    try:cp=code.index("\n",cp)
    except ValueError:break
  cp+=1
if debug:print(f"\n{tape}\npointing at {dp+1}\nwith claw holding {claw}\n{len(code)} bytes")