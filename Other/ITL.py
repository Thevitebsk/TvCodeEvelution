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
class ITL():
    def lex(self,x:str):
        #Make every command as an entry to the mapper 
        global p,n
        o="";keys={
            0  :[":"],    #Non-argumented keywords
            1  :["f"],    #One-argumented keywords
            "b":["give"], #Keywords that take a bracket (such as parenthesis) as an argument
            };ts="()<>,:";mapper={}
        [o:=o+i if i not in ts else o+f" {i} "for i in x];y=o.strip().split()
        while p<len(y):
            #Get rid of comments and empty elements in "y"
            if y[p]!="(":
                if y[p]=="<":
                    y[p:y.index(">",p)+1]=""
                    if len(y)!=0: p=-1
                    else: break
                elif y[p]in[""]:y[p]=""
            else:...
            p+=1

        p=0
        while p<len(y):
            #Check type of keyword
            o=""
            if y[p]in keys[0]:
                try:mapper[y[p]][0].append(n)
                except KeyError:mapper[y[p]]=[[n],"KEYWORD"]
            elif y[p]in keys[1]:
                try:
                    mapper[y[p]+" "+y[p+1]][0].append(n)
                    p+=1;y[p]=""
                except KeyError:
                    mapper[y[p]+" "+y[p+1]]=[[n],"KEYWORD"]
                    p+=1;y[p]=""
            elif y[p]in keys["b"]:
                try:
                    mapper[y[p]][0].append(n)
                except KeyError:
                    [o:=o+i+" "if i in"(),"else o+i for i in y[p+2:y.index(")",p)]]
                    mapper[y[p]+y[p+1]+o+y[y.index(")",p)]]=[[n],"COMMAND"]
                    p=y.index(")",p);y[p:y.index(")",p)]=""
            else:
                try:mapper[y[p]][0].append(n)
                except KeyError:mapper[y[p]]=[[n],"ID"]
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
ITL(c)
