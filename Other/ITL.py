from sys import argv
p=n=f=debug=0;a=1
try:c=open(argv[1]).read()
except IndexError:f=1;c=""
except FileNotFoundError:
    if argv[1][0]!="-":print("ITL: The file selected doesn't exist\n");exit()
    else:c="";f=1
else:a=2
try:
    if argv[a][0]=="-":
        a=argv[a:]
        while 1:
            try:a
            except IndexError:break
            else:
                if a[0]in["-d","--debug"]: debug=1
                elif a[0]in["-h","--help"]: print("ITL Line Structure:"+" "*15+"Arguments:",
                "py GSL <FILENAME> <ARGUMENTS>     -d --debug   Shows debug info",
                " "*34+"-h --help    Shows this help message",sep="\n");exit()
                else:print("Structure incorrect:\nExpected:  py GSL <FILENAME> <ARGUMENTS>",
                f"Got:       {" ".join(argv)}",sep="\n");exit()
            a.pop(0)
except IndexError:...

# The actual implementation:
class Interactive_Thon_Langauge():
    def lex(self,x:str)->list:
        #Make every command as an entry to the mapper 
        p=m=n=0;o="";mapper=[]
        keys={
            0  :[":"],         #Non-argumented keywords
            1  :["f","r"],     #One-argumented keywords
            "A":["give"]       #Any ammount of arguments
        };ts="<:;"
        for i in x:
            if i=="\"":o+=i;m=int(not m)
            elif i in ts: o+=f" {i} "
            elif i in"()>": o+=f" {i}"
            elif i in",":
                if not m:o+=f" {i} " 
                else:o+=i
            else: o+=i
        y=o.strip().split()
        while p<len(y):
            #Get rid of comments and empty elements
            if y[p]=="<":
                y[p:y.index(">",p)+1]=""
                if len(y)!=0: p=-1
                else: break
            elif y[p]=="":y[p]="\""
            elif y[p]==":":y.insert(p+2,y[p+1][1:]);y[p+1]=y[p+1][0]
            else:...
            p+=1

        p=0
        while p<len(y)-1:
            #Check type of keyword
            o=""
            if y[p]in keys[0]:mapper.append(y[p])
            elif y[p]in keys[1]:
                    mapper.append(y[p]+" "+y[p+1])
                    p+=1;y[p]=""
            elif y[p]in keys["A"]:
                    mapper.append("".join(y[p])+" ( "+" ".join(y[p+1:y.index(")",p)+1])[1:])
                    p=y.index(")",p)+1
            else:mapper.append(y[p])
            n+=1;p+=1
        print(mapper)if debug else...;return mapper

    def run(self,x:list):
        def is_int(x):
            try:int(x)
            except ValueError:return False
            else:return True
        funcs={};p=0
        while p!=len(x):
            y=x[p].split(" ")
            if y[0]=="f"and x[p+1][0]==":":funcs[y[1]]=[p,x[p+3].split(",")];p+=1
            elif y[0]=="give"and y[1]=="(":
                z=" ".join(y[2:y.index(")")]).split(">")
                for i in z:
                    try:
                        if i[0]=="\"":
                            print(i.replace("\"","")],end=" ");m=1
                            if i[0]!="\""and m:print(i.replace("\"",""),end=" ")
                            elif i[0]=="\""and m:print();m=0
                        elif is_int(i):print(i)
                        else:print("...")
                    except IndexError:print("...")
            p+=1
        if debug:print(funcs)

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
if f:
    while (i:=input("Interactive Thon Langaugeㅣ")):c+=i
    Interactive_Thon_Langauge(c)
else:Interactive_Thon_Langauge(c)
