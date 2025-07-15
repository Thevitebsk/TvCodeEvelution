#okXk.py

# --UNAI v1.0-- #
stack=[];tempstack=[];point=force=0;code=input()
def push_int():
    global point
    while 1:
     if point+1>len(code):break
     tempstack.append(code[point]);point+=1
     if code[point]not in list(map(str,range(10))):point-=1;break
    stack.append("".join(tempstack));tempstack.clear()
while len(code)>point:
    if code[point]in list(map(str,range(10))):push_int()
    elif code[point]==".":print(stack.pop());force=1
    elif code[point]=="\"":
        point+=1
        while code[point]!="\"":tempstack.append(code[point]);point+=1
        stack.append("".join(tempstack));tempstack.clear()
    elif code[point]=="#":stack.pop()
    elif code[point]=="$":stack.append(stack.pop(len(stack)-2))
    elif code[point]==",":stack.append(input())
    elif code[point]=="[":point=code.index("]",point)
    point+=1
if force==0:print("\n".join(stack))
