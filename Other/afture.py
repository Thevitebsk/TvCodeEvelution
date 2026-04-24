#wKJr.py
#brother to the branjunk language

#examples
#+++++++*---*+++++++**+++*++++++++*--------*+++*------*%+++*/ - hello world
print("afftur\na brother to branjunk")
ac=mem=0
while 1:
    ac=0
    while 1:
        for c in input("\n>> "):
            if c == "+":   ac += 1
            elif c == "-": ac -= 1
            elif c == "*": print(ac)
            elif c == "/": break
            elif c == "%": mem=ac; ac=0
            elif c == "?": mem=int(input())
            elif c == "`": print(mem,end=" ")
