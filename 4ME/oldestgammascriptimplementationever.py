#RnmR.py + 5lMx.py
def main():
    content = ""
    with open('test.ger') as file:
        content = file.read()
main()
class Lexer(object):
    def __init__(self, source_code):
        self.source_code=source_code
