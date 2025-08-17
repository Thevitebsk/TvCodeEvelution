#d9Dp.py
#tried to implement the esolang "1^"

c=str("""32>|""")
p=0;s=[]
print("1^")
while True:
  if c[p]in list(map(str,range(10))):s.append(int(c[p]))
  elif c[p]==">":
    if s.pop()>s.pop():pass
    else:p+=1
  elif c[p]=="|":break
  elif c[p]=="n":
    while c[p]!="\n":p+=1
  elif c[p]=="\n"or len(c)<p:
    print(c[p])
    while c[p]!="\n"or p!=0:p-=1
  print(c[p]);p+=1
print(s)
