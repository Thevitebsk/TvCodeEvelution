# Afftur
# brother to the branjunk language

print("afftur\na brother to branjunk")
while 1:
    ac=mem=p=0
    i=input("\n>>")
    while p<len(i)and i[p]!="/":
        if i[p]=="+":   ac += 1
        elif i[p]=="-": ac -= 1
        elif i[p]=="*": print(ac)
        elif i[p]=="?": mem=int(input())
        elif i[p]=="%": mem,ac=ac,mem
        elif i[p]=="`": print(mem,end=" ")
        p+=1