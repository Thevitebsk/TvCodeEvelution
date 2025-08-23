#wKJr.py
#brother to the branjunk language

#+ adds 1 to the acumulator
#- subtacts 1 to the acumulator
#* prints the acumulator
#/ ends the program
#% stores the acumulator to a memory variable and sets the acumulator to 0
#? Gets user input and gets stored to the memory
#` Prints the memory
#examples
#+++++++*---*+++++++**+++*++++++++*--------*+++*------*%+++*/ - hello world
print("afftur\na brother to branjunk")
optime=0
code=[]
ac=0
global end
end=0
mem=0
def a():
    global ac
    ac += 1
def m():
    global ac
    ac -= 1
def p():
    global ac
    print(ac)
def store():
    global ac
    global mem
    mem=ac
    ac=0
def ui():
    global mem
    mem=int(input())
def iq():
    print(mem)
while True:
    end=0
    ac=0
    i=input("\n>>")
    while end < 1:
        for c in i:
            if c == "+" and "+" not in code:
                a()
            if c == "-" and "-" not in code:
                m()
            if c == "*" and "*" not in code:
                p()
            if c == "/" and "/" not in code:
                end=1
            if c == "%" and "%" not in code:
                store()
            if c == "?" and "?" not in code:
                ui()
            if c == "`" and "`" not in code:
                iq()
