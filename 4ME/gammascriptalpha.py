#this version of gammascript is really incomplete and will probably never will be complete
class gs(object):
    def __init__(self,code):
        self.code=code
        er=self.run(self.tokenize(code))
        try:int(er);print("-"*32,"PROGRAM ENDED AND RETURNED AN ERROR")
        except (ValueError,TypeError):0
        else:0
    def tokenize(self,code):
        tokes=[]
        pointer=0
        code=code.replace("{"," { ").replace("}"," } ").split()
        while pointer!=len(code):
            if code[pointer]=="write":
                tokes.append(["print",code[pointer]])
            elif code[pointer]in"{}":
                tokes.append(["bracket",code[pointer]])
            else:
                tokes.append(['id',code[pointer]])
            pointer+=1
        return tokes
    def run(self,tokes:list):
        pointer=0
        while pointer!=len(tokes):
            if tokes[pointer][0]=="print":
                if tokes[pointer+1][0]!="bracket":
                    print("Incorrect Syntax!");return 1
                pointer+=2
                while tokes[pointer][0]!="bracket":
                    print(tokes[pointer][1],end=" ")
                    pointer+=1
            pointer+=1
with open('C:\\Users\\Глеб\\AppData\\Roaming\\Code\\User\\History\\-517b750d\\0gmT.gr')as file:
    gs(file.read())
