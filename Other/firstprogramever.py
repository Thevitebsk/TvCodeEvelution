def out():
    sentence=input("Input a sentence:")
    print(sentence)
def condition():
    conditionif=input("Input a condition:")
    conditionaction=input("Input an action:")
    conditionelseaction=input("Input an action:")
    print("if"), print(conditionif)
    print(conditionaction)
    print("else")
    print(conditionelseaction)
therm=input("Input a code:")
if therm=="out":
    out()
elif therm=="condition":
    condition()
