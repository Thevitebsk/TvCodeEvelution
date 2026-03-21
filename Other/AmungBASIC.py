import typing
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

(PROTOTYPE, CREATOR MAY LEAK THIS IF HE WANTS TO)
======================================================================
AmungBASIC VERSION 3.1 3,5 inch floppy disk""")
class AmungBASIC(object):
    def split_all(self,string:str,symbols:list[str]):
        for _ in symbols:
            string=string.replace(_,f' {_} ')
        return string
    def __init__(self,code):
        for _ in code:
            try:
                int(self.run(self.tokenize(_)))
                print("\n"+"-"*32+"\nPROGRAM ENDED AND RETURNED AN ERROR")
            except(ValueError,TypeError):0
    def tokenize(self,code):
        tokes=[]
        pointer=0
        code=self.split_all(code,["=","[","]"]).split()
        while pointer!=len(code):
            if code[pointer]=="print":
                tokes.append("print")
            elif code[pointer]in"[]":
                tokes.append("bracket")
            else:
                tokes.append(['id',code[pointer]])
            pointer+=1
        return tokes
    def run(self,tokes:list):
        pointer=0
        while pointer!=len(tokes):
            if tokes[pointer]=="print":
                if tokes[pointer+1]!="bracket":
                    print("Incorrect Syntax!");return 1
                pointer+=2
                while tokes[pointer]!="bracket":
                    print(eval(tokes[pointer][1]),end=" ")
                    pointer+=1
            pointer+=1
def unbounded_insert(list:list,index:int,object:typing.Any)->None:
  try:
    int(index)
    list+=["0"]*(int(index)-len(list))
    list[int(index)-1]=" ".join(object)
    return list
  except(ValueError,TypeError):
    raise TypeError(
      "Index must be an int, str was given instead"
    )
while 1:
  i=input("f:")
  if i=="run":
    if lines:
      AmungBASIC(lines)
      print()
    else:
       print("No lines to run!")
  elif i=="wipe": lines.clear()
  else:
    unbounded_insert(lines,i.split()[0],i.split()[1:])
