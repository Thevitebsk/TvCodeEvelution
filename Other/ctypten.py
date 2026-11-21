#pretty unfinished considering idk how to do nested loops
#also this code is from september 5th
code="";p=0
matrix=[[0]*25]*25;x=y=0
i=input("input raw data:")
for byte in i:
    code+=(hex(ord(byte)+int("f0000",16))[3:])
while len(code)>p:
    matrix[y][x]%=2**16
    y%=25;x%=25
    print(code[p],x,y,matrix[y][x],sep=" ")
    if code[p]=="0":...
    elif code[p]=="1":matrix[y][x]+=1
    elif code[p]=="2":matrix[y][x]-=1
    elif code[p]=="3":x-=1
    elif code[p]=="4":y+=1
    elif code[p]=="5":x+=1
    elif code[p]=="6":y-=1
    elif code[p]=="7":y=x=0
    elif code[p]=="a":
        try:matrix[y][x]=int(input())
        except ValueError:print("NaN");break
    elif code[p]=="b":
        print(chr(matrix[y][x]))
    elif code[p]=="c":
        print(matrix[y][x])
    elif code[p]=="d":
        matrix[y+1][x]+=matrix[y][x]
        matrix[y][x]=0
    elif code[p]=="f":break
    elif code[p]=="e":
        matrix[y][x]=ord(input()[0])
    else:print(f"{code[p]} not defined... yet")
    p+=1
