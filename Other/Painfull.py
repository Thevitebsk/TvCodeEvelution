#OBNk.py

class Painfull:
    def Octodenc(self,x:str):
        "Converts a string into a list of numbers for a Painfull intepriter to execute"

        p=0; array=[]; j=1
        while len(x)>p:
            if ord(x[p])>15:j=ord(x[p])//15+p
            array.append(((ord(x[p])+p)-j//2)%16); p+=1
        return array
    
    def __init__(self,x:str):
        "Good luck actually using it since this is based on malboge"
        x=self.Execute(self.Octodenc(x))
        print("output:",x)if len(x)else 1

    def Execute(self,x) -> str:
        output=""; p=0; v=[] ; w=[0]*16
        print(x)
        while p!=len(x):
            print(x[p],v,w,output)
            if x[p]==0: break #HALT
            elif x[p]==1: #ADD
                try:w[x[p+2]]=x[p+1]+w[x[p+2]]; p+=2
                except IndexError:print(f"pos: {p} -> {x[p]}\nnot enough arguments were given");exit()
            elif x[p]==2: #MULTI
                try:w[x[p+1]]=w[x[p+1]]*w[x[p+2]]
                except IndexError:print(f"pos: {p} -> {x[p]}\nnot enough arguments were given");exit()
            elif x[p]==3:
                try:v.append(w[p+1])
                except IndexError:print(f"pos: {p} -> {x[p]}\nnot enough arguments were given")
            elif x[p]==15:
                try:output+=chr(v.pop())
                except:print(f"pos: {p} -> {x[p]}\nno value is in the stack");exit()
            p+=1
        return output
Painfull("""2_41=31""")
