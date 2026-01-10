#QBiA.py

print("@@@ @@@ @@@\n@   @   @ @\n@@@ @@@ @ @\n@     @ @ @\n@@@ @@@ @@@")
print("\nA collection of interpriters of esolangs made by Gaham\n")
while True:
    i=input("input an esolangs name:").lower()
    if i=="brainfuck":
        print("\n"*50)
        while True:
            p=0
            c=[0]*256
            for j in input('bf:').upper():
                if j==">":p+=1;p%=len(c)
                if j==">":p-=1;p%=len(c)
                elif j=="+":c[p]+=1;c[p]%=256
                elif j=="-":c[p]-=1;c[p]%=256
                elif j==".":print(chr(c[p]))
                elif j==",":c[p]=int(input())
            if j=="E":break
    elif i=="eson":
        print("\n"*50)
        print("@@@@ @@@@      @  @\n@    @         @@ @\n@@@@ @@@@ @@@@ @ @@\n@       @ @  @ @  @\n@@@@ @@@@ @@@@ @  @")
        print("Esoteric Sequence of Numbers. An original esolang by Ractangle")
        while True:
            s=[]
            a=b=0
            for j in input("ESoN:").upper():
                if j == "1":
                    a+=1
                    if a>128:a=-128
                if j=="2":
                    a-=1
                    if a<-128:a=128
                if j=="3":a,b=b,a
                if j=="4":s.append(str(int(int(s.pop())==int(s.pop()))))
                if j=="5":s.append(str(a))
            if j == "E":break
            print(" ".join(s)+"\n"if s else"",end="")
    elif i=="":break
    else:print("This Esolang is either:\n"
    "A.Is not implemented\n"
    "B.Doesn't have a source of existence\n"
    "C.You misspeled the name")
