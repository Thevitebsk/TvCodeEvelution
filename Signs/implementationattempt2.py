#GhcQ.py
#again, another attempt at implementing Signs (for more info look here:https://esolangs.org/wiki/%E2%8A%97)

#*******<Commands>*******
TT_INT="INT"
TT_FLOAT="FLOAT"
class Priority_road:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self, type, value):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
