#0GDw.py
#me just having with for loops i guess?

def OSIC(a,b,c):
    o=[a,b,c]
    a*=b
    c+=a
    print(o[((a*b)//c)%3],end=",")

len=int(input("how many numbers do you need?:"))
for a2 in range(1,len+1):
    for b2 in range(1,len+1):
        for c2 in range(1,len+1):OSIC(a2,b2,c2)
        if c2==len:print(f"\t{a2} {b2}\n");s=0
