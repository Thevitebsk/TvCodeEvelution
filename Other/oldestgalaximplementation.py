#soDa.py

#>* Adds one and multiples by 2
#<< decrements the value by two
#^ outputs the ASCI character of the value
oc=0
char = chr(oc)
while True:
    i=input(">>")
    if ">*" in i:
        oc=oc + 1
        oc=oc * 2
        print(oc)
    elif i in "<<":
        oc=oc-2
        print(oc)
    elif i in "^":
        print(char)
