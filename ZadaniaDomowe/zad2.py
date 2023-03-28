l1 = int(input("Podaj 1 liczbe: "))
l2 = int(input("Podaj 2 liczbe: "))
operator = input("Podaj operator [+ - * /] : ")

if operator == "+" :
    print(l1+l2)
elif operator == "-" :
    print(l1-l2)
elif operator == "*" :
    print(l1*l2)
else :
    print(l1/l2)

