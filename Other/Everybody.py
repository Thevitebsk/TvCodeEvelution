# Everybody! - langauge inspred by "@everyone" (see https://esolangs.org/wiki/@everyone for more info about "@everyone")
import sys
print("Everybody!")
variables={}
try:code = open(sys.argv[1]).readlines()
except IndexError:print("no file was used"); exit()

p=0
while p!=len(code): code[p]=code[p].replace("\n",""); p+=1

p=0
try:
    while code[p]!="Hello everyone!": p+=1
except IndexError:
    raise Exception("\nERROR INFO:\n"+
                   "No starting point found")
while p!=len(code):
    if code[p][0]=="@"and code[p].split(" ")[0][-1]==","and" ".join(code[p].split(" ")[1:])=="at least say something":
        variables[code[p].split(" ")[0][1:-1]]=input()
        print(variables)
    p+=1
