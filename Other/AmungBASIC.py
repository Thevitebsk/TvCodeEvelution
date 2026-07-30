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

======================================================================""")
class AmungBASIC:
    def __init__(self,code):
        for _ in code:
            run=self.run(self.tokenize(_))
            if run!=0:print(
              "\n"+"-"*32,
              "PROGRAM ENDED AND RETURNED AN ERROR",
              run,sep="\n",end=""
            );break
    def tokenize(self,code):
        t=[]
        p=0
        for _ in "=[]!`": code=code.replace(_,f' {_} ')
        code=code.split()
        while p!=len(code):
            if code[p] in["print","`"]: t.append("print")
            elif code[p] in"[]": t.append("bracket")
            elif code[p] in["!","remind"]: t.append("remind")
            else: t.append(['id',code[p]])
            p+=1
        return t
    def run(self,t:list)->str|int:
        p=0
        while p!=len(t):
            
            if t[p:p+2]==["print","bracket"]:
                p+=2
                while p!=len(t)and t[p]!="bracket":
                    print(eval(t[p][1]),end=" "); p+=1

                if p==len(t):return "Syntax: Unclosed bracket"
                    
            if t[p]=="remind": break
            p+=1
        return 0
def to_line(x):
    global lines
    try:
      a=int(x.split()[0])
      if a>0:
        if a-len(lines)>0:lines+=[""]*(a-len(lines))
        lines[a-1]=" ".join(x.split()[1:])
      else:raise SyntaxError(
        "Error parsing the line,\n"
        "Line numbers must be a positive interger!"
       )
    except(ValueError,TypeError):
      raise SyntaxError(
        "Error parsing the line,\n"
        "Have you wrote the wrong command"
        "or have you forgoten a line number?"
      )
while(i:=input("f:"))!="exit":
  if i=="run":
    if lines:
      AmungBASIC(lines)
      print()
    else:
      print("No lines to run!")
  elif i=="wipe": lines.clear()
  elif i=="list":
    if not lines: print("Program is empty!")
    else:
      n=0
      for i in lines:
        n+=1
        if lines and i: print(n,i)
  elif i=="open":
    while not lines and(i:=input("o:"))!="":
      lines=[]
      for i in open(f"{i}").readlines():
        to_line(i)
  else: to_line(i)