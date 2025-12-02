#aoc 2025 day 2 submission by gaham!
#part 1
IDs=input().split(",");LIDs={};IIDs=[]
for i in IDs:
    LIDs[(x:=i.split("-"))[0]+"-"+x[1]]=list(map(int,range(int((x:=i.split("-"))[0]),int(x[1])+1)))
for i in LIDs:
    for j in LIDs[i]:
        if str(j)[:len(str(j))//2]==str(j)[len(str(j))//2:]:IIDs.append(j)
print(f"SUM OF INVALID ID'S: {sum(IIDs)}")
