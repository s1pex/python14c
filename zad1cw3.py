stringLiczb = input("Podaj liczby rozdzielone przecinkiem: ")
listaNumerow = [int(n) for n in stringLiczb.split(",")]

minVal = listaNumerow[0]
maxVal = listaNumerow[0]
for num in listaNumerow:
    if num < minVal:
        minVal = num
    if num > maxVal:
        maxVal = num

print("Wartość minimalna:", minVal)
print("Wartość maksymalna:", maxVal)
