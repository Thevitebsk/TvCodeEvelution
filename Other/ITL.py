from sys import argv
p=n=debug=0
try:c=open(argv[1]).read()
except IndexError:print("ITL: No file was used (temp)");exit()
except FileNotFoundError:print("ITL: The file selected doesn't exist");exit()
try:
    if argv[2][0]=="-":
        args=argv[2:]
        while 1:
            try:args
            except IndexError:break
            else:
                if args[0]in["-d","--debug"]: debug=1
                elif args[0]in["-h","--help"]: print("ITL Line Structure:"+" "*15+"Arguments:",
                "py GSL <FILENAME> <ARGUMENTS>     ""-d --debug   Shows debug info",
                " "*34+"-h --help    Shows this help message",sep="\n");exit()
                else:print("Structure incorrect:","Expected:  py GSL <FILENAME> <ARGUMENTS>",
                f"Got:       {"py "+" ".join(argv)}",sep="\n");exit()
            args.pop(0)
except IndexError:...

# The actual implementation:
class MusuM():
    def lex(self,x:str):
        #Make every command as an entry to the mapper 
        global p,n
        o="";keys="f";ts="()<>,:";mapper={}
        [o:=o+i if i not in ts else o+f" {i} "for i in x];y=o.strip().split()
        while p<len(y):
            if y[p]=="<":
                y[p:y.index(">",p)+1]=""
                if len(y)!=0: p=-1;n=0
                else: break
            elif y[p]in[""]:y[p]=""
            elif y[p]in[ts,keys]:
                try:mapper[f"{y[p]}"][0].append(n)
                except KeyError:mapper[f"{y[p]}"]=[[n],"KEYWORD"]
            else:
                try:mapper[f"{y[p]}"][0].append(n)
                except KeyError:mapper[f"{y[p]}"]=[[n],"ID"]
            n+=1;p+=1
        if debug:print("Command map:",mapper)

    def __init__(self,code):
        self.code=code
        self.lex(code)

print("""
@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@
 @    @@@   @@@
      @@@   @@@
 @    @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@
@@@   @@@   @@@@@@
@@@   @@@   @@@@@@
"""[1:-1])
MusuM(c)
