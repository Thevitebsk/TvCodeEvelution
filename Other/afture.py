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
optime=ac=end=mem=0
while 1:
    end=ac=0;i=input("\n>>")
    while end < 1:
        for c in i:
            if c == "+":   ac += 1
            elif c == "-": ac -= 1
            elif c == "*": print(ac)
            elif c == "/": end=1
            elif c == "%": mem=ac; ac=0
            elif c == "?": mem=int(input())
            elif c == "`": print(mem)
