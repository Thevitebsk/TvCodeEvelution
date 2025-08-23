#U8LL.py + MPUG.py
#this version of gammascript is really incomplete and will probably never will be complete
import re
class Lexer(object):
    def __init__(self, source_code):
        self.source_code=source_code
    def tokenize(self):
        token=[]
        source_code=self.split()
        source_index=0
        while source_index<len(source_code):
            word = source_code[source_index]
            if word == "write":
                token.append(["WRITE", word])
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                token.append(['IDENTIFIER', word])
            elif re.match('[0-9]', word):
                token.append(['IDENTEGER', word])
            source_index +=1
        print(token)
        return token
def main():
    content = ""
    with open('test.gr') as file:
        content = file.read()
    lex=Lexer(content).tokenize()
main()
