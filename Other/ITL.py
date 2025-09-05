from sys import argv
p=debug=0
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
                "py GSL <FILENAME> <ARGUMENTS>     -d --debug   Shows debug info",
                " "*34+"-h --help    Shows this help message",sep="\n");exit()
                else:print("Structure incorrect:\nExpected:  py GSL <FILENAME> <ARGUMENTS>",
                f"Got:       {" ".join(argv)}",sep="\n");exit()
            args.pop(0)
except IndexError:...

# The actual implementation:
class ITL():
    def lex(self,x:str)->list:
        #Make every command as an entry to the mapper 
        z=[];p=n=0;o=q="";keys={
            0  :[":"],         #Non-argumented keywords
            1  :["f"],         #One-argumented keywords
            "A":["give"],      #Any length
            "<":["(",")"]      #Space added before the symbol
            };ts="<>,:";mapper={}
        [o:=o+i if i not in ts else o+f" {i} "for i in x];[q:=q+i if i not in keys["<"]else q+f" {i}"for i in o]
        y=q.strip().split()
        while p<len(y):
            #Get rid of comments and empty elements
            if y[p]=="<":
                y[p:y.index(">",p)+1]=""
                if len(y)!=0: p=-1
                else: break
            elif y[p]=="":y[p]=""
            else:...
            p+=1

        p=0
        while p<len(y)-1:
            #Check type of keyword
            o=""
            if y[p]in keys[0]:
                try:mapper[y[p]].append(n)
                except KeyError:mapper[y[p]]=[n]
            elif y[p]in keys[1]:
                try:
                    mapper[y[p]+" "+y[p+1]].append(n)
                    p+=1;y[p]=""
                except KeyError:
                    mapper[y[p]+" "+y[p+1]]=[n]
                    p+=1;y[p]=""
            elif y[p]in keys["A"]:
                try:
                    mapper["".join(y[p])+" ( "+" ".join(y[p+1:y.index(")",p)+1])[1:]].append(n)
                    p=y.index(")",p)+1
                except KeyError:
                    mapper["".join(y[p])+" ( "+" ".join(y[p+1:y.index(")",p)+1])[1:]]=[n]
                    p=y.index(")",p)+1
            else:
                try:mapper[y[p]].append(n)
                except KeyError:mapper[y[p]]=[n]
            n+=1;p+=1
        [z.append([i[0],i[1]])for i in list(mapper.items())]; return z

    def run(self,x:list):
        funcs={};p=0
        while p!=len(x):
            y=x[p][0].split(" ");print(y)
            if y[0]=="f"and x[p+1][0]==":":
                funcs[y[1]]=p;p+=1
            elif y[0]=="give"and y[1]=="(":
                z=" ".join(y[2:y.index(")")]).split(",")
                for i in z:
                    if i[0][-1]=="\"":print(i[1:-1])
            p+=1
        print(funcs)

    def __init__(self,code): self.run(self.lex(code))
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
