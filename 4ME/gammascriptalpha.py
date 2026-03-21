#this version of gammascript is really incomplete and will probably never will be complete
class gs(object):
    def __init__(self,code):
        try:int(self.run(self.tokenize(code)));print(
         "\n"+"-"*32,"\nbPROGRAM ENDED AND RETURNED AN ERROR"
        )
        except (ValueError,TypeError):0
    def tokenize(self,code):
        tokes=[]
        pointer=0
        code=code.replace("{"," { ").replace("}"," } ").split()
        while pointer!=len(code):
            if code[pointer]=="write":
                tokes.append("print")
            elif code[pointer]in"{}":
                tokes.append("bracket")
            else:
                tokes.append(['id',code[pointer]])
            pointer+=1
        return tokes
    def run(self,tokes:list):
        pointer=0
        while pointer!=len(tokes):
            if tokes[pointer]=="print":
                if tokes[pointer+1]!="bracket":
                    print("Incorrect Syntax!");return 1
                pointer+=2
                while tokes[pointer]!="bracket":
                    print(tokes[pointer][1],end=" ")
                    pointer+=1
            pointer+=1
gs("write{smth}")
