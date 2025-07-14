#v9ku.py
#take two of the the alpha version

import time
import re
i="""create var x is 1
if x is 1 then:
write 1"""
print("gammascript v0.2")
rem="write "
variables = {}
parts = i.split()
def create():
    if len(parts) >= 4 and parts[0] == "create" and parts[1] == "var" and parts[3] == "is":
        variable_name = parts[2]
        variable_value = ' '.join(parts[4:])
        variables[variable_name] = variable_value
def write():
    if len(parts) >= 1 and parts[0] == "write":
        word = parts[1:]
        print(word)
def ifcon():
    if len(parts) >= 5 and parts[0] == "if" and parts[2] == "is" and parts[4] == "then:":
        variable_name = parts[1]
        variable_value = ' '.join(parts[3])
        excution = parts[5:]
        var=variable_name + variable_value
        print(var,"?")
        i2=input(">>")
        if i2 in "write":
             write()
        if i2 in "create":
            create()
        if i2 in "if":
            print("gammascript can't hold more then nesting idiot")
def wait(timed):
    if len(parts) >= 1 and parts[0] == "wait":
        time.sleep(timed)
if "create" in i:
    create()
if "write" in i:
    write()
if "if" in i:
    ifcon()
