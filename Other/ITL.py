from sys import argv
p=n=0
try:c=open(argv[1]).read()
except (IndexError,FileNotFoundError):print("False");exit()

# The actual implementation:
class MusuM():
    def lex(self,x:str):
        global p,n
        o="";keys="f";ts="()<>,:";lexed={};[o:=o+i if i not in ts else o+f" {i} "for i in x];y=o.strip().split()
        while p<len(y):
            if y[p]=="<":
                y[p:y.index(">",p)+1]=""
                if len(y)!=0: p=-1;n=0
                else: break
            elif y[p]in[""]:y[p]=""
            elif y[p]in[ts,keys]: lexed[f"{y[p]}{n}"]="KEYWORD"
            else: lexed[f"{y[p]}{n}"]="ID"
            n+=1;p+=1
        print(lexed)
    def __init__(self,code):
        self.code=code
        self.lex(code)

print("""
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
@@@   @@@   @@@
@@@   @@@   @@@
 @    @@@   @@@
      @@@   @@@
 @    @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@@@@
@@@   @@@   @@@@@@
"""[1:-1])
MusuM(c)
