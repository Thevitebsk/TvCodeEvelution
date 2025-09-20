from sys import argv
p=f=debug=0;n=a=1
try:c=open(argv[1]).read()
except IndexError:f=1;c=""
except FileNotFoundError:
    if argv[1][0]!="-":print("ITL: The file selected doesn't exist");exit()
    else:c="";f=1
else:a=2
try:
    if argv[a]=="-h":
        print("ITL for begineers!",
              "To make a program using the REPL. "
              "\nMake sure to not include a file name, "
              "else the code from the file will be executed",
              "Once your at the REPL, \nlocate the \"1: \" text, "
              "this is where you put your line of code (e.g. give(\"hi!\"))",
              "And to execute your program in the REPL,\n"
              "you just input \"end\" to the code line input"
              ,sep="\n\n");exit()
    elif argv[a][0]=="-":
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
            0:[":"],             #Non-argumented keywords
            1:["f","r","give"],  #One-argumented keywords
        };ts="<:;"
        for i in x:
            if i=="\"":m=int(not m)
            if not m:
                if i in ts: o+=f" {i} "
                elif i in"()>": o+=f" {i}"
                elif i in",":o+=i
                else: o+=i
            elif m:o+=i
        y=o.strip().split()
        while p<len(y):
            #Get rid of comments and empty elements
            if y[p]=="<":
                y[p:y.index(">",p)+1]=""
                if len(y)!=0: p=-1
                else: break
            elif y[p]=="":y[p]="\""
            elif y[p]==":":
              try:y.insert(p+2,y[p+1][1:]);y[p+1]=y[p+1][0]
              except IndexError:print("ITL: Name Error |"
                " No function name was given");exit()
            else:...
            p+=1

        p=0
        while p<len(y):
            if y[p]in keys[0]:mapper.append(y[p])
            elif y[p]in keys[1]:
                    mapper.append(y[p]+" "+y[p+1])
                    p+=1;y[p]=""
            else:mapper.append(y[p])
            n+=1;p+=1
        print(mapper)if debug else...;return mapper

    def run(self,x:list):
        print(x)
        def is_int(x):
            try:int(x)
            except ValueError:return False
            else:return True
        funcs={};p=0
        while p!=len(x):
            y=x[p].split(" ")
            if y[0]=="f"and x[p+1][0]==":": funcs[y[1]]=p;p+=1
            elif y[0]=="give"and y[1]=="(":
                z=" ".join(y[2:y.index(")")]).split(">")
                for i in z:
                    try:
                        if i[0]=="\"":
                            print(i[1:-1],end=" ");m=1
                            if i[0]!="\""and m:print(i.replace("\\\"","\\e"),end=" ")
                            elif i[0]=="\""and m:print();m=0
                        elif is_int(i):print(i)
                        else:print("ITL: Invalid type");exit()
                    except IndexError:print("ITL: Invalid type");exit()
            p+=1
        if debug:print(funcs)

    def __init__(self,code): self.run(self.lex(code))
print("""
@@@@########!!!
@@@@########!!!
 @    ###   !!!
      ###   !!!
 @    ###   !!!
@@@   ###   !!!
@@@   ###   !!!
@@@   ###   !!!
@@@   ###   !!!
@@@   ###   !!!!!!
@@@   ###   !!!!!!
"""[1:-1])
if f:
    while (i:=input(f"{n}: "))!="end":c+=i+"\n";n+=1
    Interactive_Thon_Langauge(c)
else:Interactive_Thon_Langauge(c)