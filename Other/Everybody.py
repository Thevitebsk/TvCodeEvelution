# Everybody! - langauge inspred by "@everyone" (see https://esolangs.org/wiki/@everyone for more info about "@everyone")

import sys
print("Everybody!")
variables={}
try:code = open(sys.argv[1]).readlines()
except IndexError:print("no file was used"); exit()

p=0
while p!=len(code): code[p]=code[p].replace("\n",""); p+=1

def evaluate(arg) -> bool:
    a=arg[0][0:-1]
    p=0
    
    ayl=a.replace("->"," -> ").split(" ")
    print(a,ayl)

    if len(ayl)==1 and ayl[0][0]=="@":
        return bool(variables[ayl[0][1::]])
    elif len(ayl)==1 and ayl[0][0]!="@":
        return bool(ayl[0])

p=0
try:
    while code[p]!="Hello everyone!": p+=1
except IndexError:
    raise Exception("\nERROR INFO:\n"+
                   "No starting point found")
while p!=len(code):
    c=code[p].strip().split(" ")
    print(c)
    if c[0][0]=="@"and c[0][-1]==","and" ".join(c[1:])=="at least say something":
        variables[c[0][1:-1]]=input()
    elif " ".join(c[0:2])=="Quick question,"and" ".join(c[-3:len(c)])=="If so, then:":
        if evaluate(c[2:-3][0:len(c)-2]):...
        else:
            while c!="" and p!=len(code):
                c=code[p].strip()
                p+=1
            p-=1
    p+=1
