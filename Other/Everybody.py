# Everybody! - formal-ish version "@everyone" (see https://esolangs.org/wiki/@everyone for more info about "@everyone")

import sys
print("Everybody!")
variables={}
try:code = open(sys.argv[1]).readlines()
except IndexError:print("no file was used"); exit()

p=0
code=[i.strip()for i in code]

def evaluate(arg)->bool:
    def is_int(x)->bool:
        try:int(x)
        except ValueError:return False
        return True
    a=arg[0][:-1]
    ayl=a.replace("->"," -> ").split(" ")

    if len(ayl)==1 and is_int(ayl[0]):
        return bool(int(ayl[0]))
    elif len(ayl)==1 and ayl[0][0]=="@":
        if is_int(variables[ayl[0][1::]]):
            return bool(int(variables[ayl[0][1::]]))
        else:
            return bool(variables[ayl[0][1::]])

p=0
try:
    while code[p]!="Hello everyone!": p+=1
except IndexError:
    raise Exception("\nERROR INFO:\n"+
                   "No starting point found")

while p!=len(code):
    c=code[p].strip().split(" ")

    if c[0][0]=="@"and c[0][-1]==","and code[p].endswith("at least say something"):
        variables[c[0][1:-1]]=input()
    
    elif code[p].startswith("Quick question,")and code[p].endswith("If so, then:"):
        if bool(evaluate(c[2:-3][0:len(c)-2])):...
        else:
            while code[p].strip().split(" ")[0]!="End" and p!=len(code): p+=1
            p-=1
    
    elif c[0]=="|":
        if c[1][0]=="@"and" ".join(c[2:5])=="is set to":
            variables[c[1][1:]]=" ".join(c[5:])
        else:...
    elif " ".join(c[0:3])=="Please go to":
        tp=p;p=0;target=c[-1]
        while (c:=code[p].strip().split(" ")[0])!=f"{target}:": p+=1

    elif " ".join(c[0:3])=="Say the number"and c[-1][-1]=="!":
        try:print(int(variables[c[-1][1:-1]]))
        except ValueError:print(f"{c[-1][1:-1]}:\n"
                               +f"| Say the number @{c[-1][1:-1]}!\n"
                                +"I am not even a number");exit()
        except KeyError:print(f"You:\nSay the number @{c[-1][1:-1]}!\n"
                              +"You:\nOh right they aren't here");exit()
    
    elif " ".join(c[0:3])=="Say the phrase"and c[-1][-1]=="!":
        try:
            if variables[c[-1][1:-1]][0]=="\"":
                print(variables[c[-1][1:-1]][1:-1],end=" ")
            else:
                print(variables[c[-1][1:-1]],end=" ")
        except KeyError:
            if c[-1][0]=="@":
                print(f"You:\nSay the phrase @{c[-1][1:-1]}!\n"
                      +"You:\nOh right they aren't here");exit()
            elif " ".join(c[3:])[0]=="\"": print(" ".join(c[3:])[1:-2])
            else: print(" ".join(c[3:]))
    p+=1
