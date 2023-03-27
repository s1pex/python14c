#1. Napisz program, który pobierze od użytkownika liczby rozdzielone przecinkiem a następnie policzy znajdzie ich max oraz min, bez używania wbudowanych funkcji. (20%)
nums = input("Podaj liczby: ")
num_list = nums.split(",")

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])

max = num_list[0]
min = num_list[0]
for number in range(len(num_list) + 1):
    if number > max :
        max = number
    else :
        min = number

print(f"najwieksza liczba: {max}")
print(f"najmniejsza liczba: {min}")
