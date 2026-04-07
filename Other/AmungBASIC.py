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
        for _ in ["=","[","]"]:
            code=code.replace(_,f' {_} ')
        code=code.split()
        while p!=len(code):
            if code[p]=="print":
                tokes.append("print")
            elif code[p]in"[]":
                tokes.append("bracket")
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
            p+=1
while(i:=input("f:"))!="exit":
  if i=="run":
    if lines:
      AmungBASIC(lines)
      print()
    else:
      print("No lines to run!")
  elif i=="wipe": lines.clear()
  elif i=="list": 
     for i in lines:
        print(lines.index(i)+1,i)if lines and i!="0"else...
  else:
    try:
      int(i.split()[0])
      lines+=["0"]*(int(i.split()[0])-len(lines))
      lines[int(i.split()[0])-1]=" ".join(i.split()[1:])
    except(ValueError,TypeError):
      raise TypeError(
        "Index must be an int, str was given instead"
      )
