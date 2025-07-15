#QBiA.py

print("@@@ @@@ @@@")
print("@   @   @ @")
print("@@@ @@@ @ @")
print("@     @ @ @")
print("@@@ @@@ @@@")
print("\nA collection of interpriters of esolangs made by Gaham\n")
cs=" !#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]`abcdefghijklmnopqrstuvwxyz{|}~"
cl=0
def cls():
    global cl
    while cl!=70:
        print("\n")
        cl+=1
    cl=0
def bf():
    cls()
    c=[0]*8
    p=0
    while True:
        p=0
        c=[0]*8
        for bfi in input('bf:'):
            if bfi==">":
                p+=1
                if p>8:
                    print("OUT OF RANGE")
                    p=0
            elif bfi=="<":
                p-=1
                if p<0:
                    p=8
                    print("OUT OF RANGE")
            elif bfi == "+":
                c[p]+=1
                if c[p]>102:
                    c[p]=0
            elif bfi == "-":
                c[p]-=1
                if c[p]==0:
                    c[p]=102
            elif bfi == ".":
                print(cs[c[p]])
            elif bfi == ",":
                c[p]=int(input("num:"))
        if bfi == "E":
            break
def eson():
    cls()
    print("@@@@ @@@@      @  @")
    print("@    @         @@ @")
    print("@@@@ @@@@ @@@@ @ @@")
    print("@       @ @  @ @  @")
    print("@@@@ @@@@ @@@@ @  @")
    print("Esoteric Sequence of Numbers. An original esolang by Ractangle")
    while True:
        ac=0
        s=[]
        global aac
        aac=0
        tv=0
        for esoni in input("ESoN:"):
            if esoni == "1":
                ac += 1
                if ac>128:
                    ac=-128
            if esoni == "2":
                print(s)
            if esoni=="3":
                ac-=1
                if ac<-128:
                    ac=128
            if esoni=="4":
                ac=tv
                acc=ac
                tv=acc
            if esoni=="5":
                print(acc)
            if esoni=="6":
                if ac==acc in s:
                    s.append(0)
                else:
                    s.append(1)
            if esoni == "7":
                s.append(ac)
            if esoni == "8":
                s.append(acc)
        if esoni == "E":
            break
while True:
    eso=input("input an esolangs name:")
    if eso=="brainfuck":
        bf()
    elif eso=="ESoN":
        eson()
    else:
        print("This Esolang is uninterpreterd or doesn't exist or you made a speling mistake")
