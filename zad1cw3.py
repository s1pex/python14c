stringLiczb = input("Podaj liczby rozdzielone przecinkiem: ")
listaNumerow = [int(n) for n in stringLiczb.split(",")]

min_val = listaNumerow[0]
max_val = listaNumerow[0]
for num in listaNumerow:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print("Wartość minimalna:", min_val)
print("Wartość maksymalna:", max_val)
