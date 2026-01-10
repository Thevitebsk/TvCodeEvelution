# Everybody! - formal-ish version "@everyone" (see https://esolangs.org/wiki/@everyone for more info about "@everyone")

import sys
print("Everybody!")
variables={}
try:code = open(sys.argv[1]).readlines()
except IndexError:print("no file was used"); exit()

p=0
code=[i.strip().replace("->"," -> ")for i in code]

def evaluate(arg)->bool:
    def is_int(x)->bool:
        try:int(x);return True
        except ValueError:return False

    a=variables[arg[1::]]
    if is_int(arg):
        return bool(int(arg))
    elif arg[0]=="@":
        return bool(int(a)if is_int(a)else a)

try:
    while code[p]!="Hello everyone!": p+=1
except IndexError:
    print("ERROR INFO:\n"
          "No starting point found");exit()

while p!=len(code):
    c=code[p].strip().split(" ")

    if c[0][0]=="@"and c[0][-1]==","and code[p].endswith("at least say something"):
        variables[c[0][1:-1]]=input()
    
    elif code[p].startswith("Quick question,")and code[p].endswith("If so, then:"):
        x=c[2:-3];x[-1]=x[-1][0:-1]
        if len(x)>1:
            x.pop(1)
            try:x[1]=evaluate(x[1])
            except IndexError:x[1]=False
        else:x.append(True)
        x[0]=evaluate(x[0])
        if x[0]==x[1]:...
        else:
            while code[p].strip().split(" ")[0]!="End"and p!=len(code): p+=1
            p-=1
    
    elif c[0]=="|":
        if c[1][0]=="@"and" ".join(c[2:5])=="is set to":
            if c[5][0]==">":variables[c[1][1:]]=chr(int(c[5][1:]))
            variables[c[1][1:]]=" ".join(c[5:])
        else:...
    elif" ".join(c[0:3])=="Please go to":
        p=0;target=c[-1]
        try:
            while (c:=code[p].strip().split(" ")[0])!=f"{target}:": p+=1
        except IndexError:print(f"ERROR INFO:\nNo label named {target} was found")
    
    elif" ".join(c[0:3])=="Say the number"and c[-1][-1]=="!":
        try:print(int(variables[c[-1][1:-1]]),end=" ")
        except ValueError:print(f"ERROR INFO:\n{c[-1][1:-1]}:\n"
                               f"| Say the number @{c[-1][1:-1]}!\n"
                                "I am not even a number");exit()
        except KeyError:print(f"ERROR INFO:\nYou:\nSay the number @{c[-1][1:-1]}!\n"
                              "\nYou:\nOh right they aren't here");exit()
    
    elif" ".join(c[0:3])=="Say the phrase"and c[-1][-1]=="!":
        try:
            if variables[c[-1][1:-1]][0]=="\"":
                print(variables[c[-1][1:-1]][1:-1],end=" ")
            elif variables[c[-1][1:-1]][0]==">":
                print(chr(int(variables[c[-1][1:-1]][1:])),end="")
            else:
                print(variables[c[-1][1:-1]],end=" ")
        except KeyError:
            if c[-1][0]=="@":
                print(f"ERROR INFO:\nYou:\nSay the phrase @{c[-1][1:-1]}!\n"
                      "\nYou:\nOh right they aren't here");exit()
            elif" ".join(c[3:])[0]=="\"": print(" ".join(c[3:])[1:-2],end=" ")
            else:
                try:print(int(" ".join(c[3:])[:-1]),end=" ")
                except ValueError:
                    print(f"ERROR INFO:\nYou:\nSay the phrase {" ".join(c[3:])}"
                          +"\nYou:\nOh right i forgot, it doesn't work like that")
    elif c[0]in["+","-","*","/"]:
        variables[c[2][1:]]=str(eval(str(variables[c[2][1:]])+c[0]+c[1]))
    p+=1
