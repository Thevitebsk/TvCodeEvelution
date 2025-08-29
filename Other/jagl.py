i="""@hi|#"""
p=m=0;s=[];v={}
while 1:
 if p==len(i):
    if not m:break
    else:
        if i in"\n":p=i.index("\n",len(" ".join(i.split()[0:-1])))
        else:p=0
 if i[p]=="@":   s.append(i[p+1:i.index("|",p)]);p=i.index("|",p)
 elif i[p]=="#": print(s.pop())
 elif i[p]=="ƒ": print(s.pop(),end="")
 elif i[p]=="~": m=1
 elif i[p]=="*": v[i[p+1]]=i[p+1:i.index("|",p)];p=i.index("|",p)
 p+=1
