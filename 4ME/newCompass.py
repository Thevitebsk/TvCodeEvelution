verdate="26th July 2025"
keywords=["f:","print"]
point=0

import sys
try:FILE=open(sys.argv[1]).read()
except:FILE=""

while point!=len(keywords)-1:
    # Removes every instance of a newline in the keywords.txt file
    keywords[point]=keywords[point].replace("\n","")
    point+=1

def LEXER(file):
    point=0
    inner=""; lex1=[]; lex2={}
    while point<len(file):
        try:
            while file[point] not in [" ", "\t", "\n"]:
                inner+=file[point]
                point+=1
            if file[point] in [" ", "\t", "\n"]:lex1.append(inner); inner=""
            else:lex1.append(file[point])
            point+=1
        except:lex1.append(inner); point=0; break
    while point<len(lex1):
        if lex1[point] in keywords:
              lex2[f"{lex1[point]} {point}"]="KEYWORD"
        elif lex1[point] in ["[","]"]:
              lex2[f"{lex1[point]} {point}"]="BRACKET"
        else: lex2[f"{lex1[point]} {point}"]="ID"
        #print(lex1[point],"->",lex2[lex1[point]])
        point+=1
    return lex2,lex1

def CHECK(file:dict):
    point=0
    """Function used for checking if a keyword"""
    print(file)
    if file[0][f"f: {point}"] and file[0][f"{file[1][point+1]} {point+1}"]=="ID": ...
    else:print(f"CHECK found an error at your formated code: \"{" ".join(file[1][point:point+2])}\", the type of the function name must be an \"ID\"")

N=1
if FILE: CHECK(LEXER(FILE)); exit()
elif not FILE:
    print("@@@@@@@  @@@@@@@"
       +"\n@ @@@ @  @@@ @@@"
       +"\n@@ @ @@  @@ @ @@"
       +"\n@@@ @@@  @ @@@ @"
       +"\n@@@@@@@  @@@@@@@"
       +"\n"
       +"\n@@@@@@@  @@@@@@@"
       +"\n@  @@@@  @@@@  @"
       +"\n@@@  @@  @@  @@@"
       +"\n@  @@@@  @@@@  @"
       +"\n@@@@@@@  @@@@@@@\n"
      +"\nCompass Console Placeholder (yes that's the actual name)"
      +f"\n{verdate}, "+
      "created by Gaham (otherwise known as Thevitebsk or User:Ractangle)")
    while 1:
        while(I:=input(f"{N}: "))!="":
            if I=="end": print("Ending sesion"); exit()
            FILE+="\n"+I; N+=1
        FILE=FILE[1::]
        if FILE!="": CHECK(LEXER(FILE))
        N=1
