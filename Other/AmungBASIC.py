lines=[]
print("""
  *                       ***
 * *                      *  *
***** ****  *  * ***  *** ***
*   * * * * *  * *  * * * *  *
*   * * * *  *** *  * *** ***
                        *
                      *
A basic-like programming language based on a Language Mockup i made in
See also:https://mockupedia.miraheze.org/wiki/AmungfBASIC

======================================================================
AmungBASIC VERSION 3.1 3,5 inch floppy disk""")
class AmungBASIC(object):
    def __init__(self,code):
        for _ in code:
            try:
                int(self.run(self.tokenize(_)))
                print("\n"+"-"*32+"\nPROGRAM ENDED AND RETURNED AN ERROR")
            except(ValueError,TypeError):0
    def tokenize(self,code):
        tokes=[]
        p=0
        for _ in ["=","[","]","!"]:
            code=code.replace(_,f' {_} ')
        code=code.split()
        while p!=len(code):
            if code[p]in["print","`"]:
                tokes.append("print")
            elif code[p]in"[]":
                tokes.append("bracket")
            elif code[p]in["!","remind"]:
                tokes.append("remind")
            else:
                tokes.append(['id',code[p]])
            p+=1
        return tokes
    def run(self,tokes:list):
        p=0
        while p!=len(tokes):
            if tokes[p]=="print":
                if tokes[p+1]!="bracket":
                    print("Incorrect Syntax!");return 1
                p+=2
                while tokes[p]!="bracket":
                    print(eval(tokes[p][1]),end=" ")
                    p+=1
            if tokes[p]=="remind": break
            p+=1
def to_line(x):
    global lines
    try:
      a=int(x.split()[0])
      if a>0:
        if a-len(lines)>0:lines+=["0"]*(a-len(lines))
        lines[a-1]=" ".join(x.split()[1:])
      else:raise TypeError(
        "Error parsing the line,\n"
        "Line numbers must be a positive natural number!"
       )
    except(ValueError,TypeError):
      raise TypeError("Error parsing the line")
while(i:=input("f:"))!="exit":
  if i=="run":
    if lines:
      AmungBASIC(lines)
      print()
    else:
      print("No lines to run!")
  elif i=="wipe": lines.clear()
  elif i=="list":
    t=0
    for i in lines:
      t+=1
      print(t,i)if lines and i!="0"else...
  elif i=="open":
    while not lines and(i:=input("o:"))!="":
      lines=[]
      for i in open(f"{i}").readlines():
        to_line(i)
  else: to_line(i)
