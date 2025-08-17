#0GDw.py
#me just having with for loops i guess?

def OSIC(a,b,c):o=[a,b,c];a*=b;c+=a;print("[",o[(a*b//c)%3],"]",end=",")
for a2 in range(1,5):
    for b2 in range(1,5):
        for c2 in range(1,5):OSIC(a2,b2,c2)
        if c2==4:print(f"\t{a2} {b2}\n");s=0
