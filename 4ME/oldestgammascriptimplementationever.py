#U8LL.py + T70I.py
import re
class Lexer(object):
    def __init__(self, source_code):
        self.source_code=source_code
    def tokenize(self):
        token=[]
        source_code=self.source_code.split()
        source_index=0
        while source_index<len(source_code):
            word = source_code[source_index]
            if word == "writetolog":
                token.append(["WRITETOLOG_DECLARATION", word])
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                token.append(['IDENTIFIER', word])
            source_index +=1
        print(token)
        return token
def main():
    content = ""
    with open('test.gr') as file:
        content = file.read()
    lex=Lexer(content)
    tokens=lex.tokenize()
main()
