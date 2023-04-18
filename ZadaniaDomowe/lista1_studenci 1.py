#Lista1

'''
UWAGA! Nie należy zmieniać nazw funkcji, oraz wartości zmiennych podanych w pliku
poza wartościami ze stringiem "PODAJ WYNIK" - w tych zmiennych należy przechowywać wynik
dotyczący poszczególnych zadań w_1, w_2 ... w_6.

Ciało funkcji wpisujemy w kodzie zamiast "pass".

Wyniki z każdego zadania powinny wyświetlać się w jednej linijce.
Nie należy wyświetlań nic poza wynikiem działania kodu z poszczególnych zadań
w kolejności tak jak w pliku.
Plik należy zapisać w postaci: imie_nazwisko_lista1.py
'''
import random

#1. Ile unikatowych elementów znajduje się w liście:
#1 pkt

lista_1 = [0,7,8,3,3,0,7,0,3]
listaElementow = []
appear = 0

for element in lista_1:
    if element not in listaElementow:
        listaElementow.append(element)
        appear = appear + 1

w_1 = appear
print(w_1)

#2. Napisz kod, który podmieni losowy znak ze stringa
s_2 = "ala ma kota"
#na '0':
#2 pkt

listaLiter = list(s_2)
znak = "0"
index = random.randint(0, len(listaLiter)-1)
listaLiter[index] = znak
newString = "".join(listaLiter)

w_2 = newString
print(w_2)


#3. Napisz kod który podmieni z lista_3 język programowania R na JS, następnie wyświetl podmieniony JS.
# Przed JS nadal musi znajdować się python w strukturze takiego samego typu jak w przykladowej lista_3.
# 2pkt
lista_3 = [[{1: 'java', 0: ('python', 'R')},'c++'],['word', 'excel']]

#for i, element in lista_3:
  #  if element == 'R':
   #     lista_3[i] = 'JS'

lista_3[0][0][0][1].replace('R', 'JS')

w_3 = lista_3
print(w_3)


#4. Jakiego typu dane z poniższych nie mogą być kluczami słownika?
#boolean,float,int,string,tuple,list,set. Odpowiedź umieśc w stringu w_4
#1 pkt

w_4 = "set, list"
print(w_4)

#5. Dla stringa wypisz
#ile razy pojawił się dany znak, w kolejności alfabetycznej.
#Użyj słownika - wynik również ma być słownikiem.
#Sprawdzamy tylko te znaki, które występują w podanym stringu.
#2 pkt

s_5 = "ala ma kota imie ma macko"
listS5 = list(s_5)
slownik = {}

for letter in s_5:
    if letter not in slownik:
        slownik[letter] = 1
    else:
        slownik[letter] += 1

w_5 = sorted(slownik.items())
print(w_5)

#6. Napisz kod który sprawdzi, czy w poprzednim stringu s_5,
#jakikolwiek znak wystąpił dokładnie 3 razy. Wyświetl Tak jeżeli wystąpił,
#Nie jeżeli nie wystąpił.
#1 pkt
def countLetters():
    if 3 in slownik.values():
        return "Tak"
    else:
        return "Nie"

w_6 = countLetters()
print(w_6)

#7. Napisz funkcję sprawdzającą czy podane słowa/zdania są palindromem
#i zwróci True lub False ( jest/ nie jest).
#Pomiń znaki nie będące literami, wielkość liter nie ma znaczenia
#3pkt

def palindrom(s):
    s = ''.join(filter(str.isalpha, s))
    s = ','.join(filter(str.isalpha, s))
    s = s.lower()

    if s == s[::-1]:
        return True
    else:
        return False

s_7_1 ="Nowy Targ, góry, Zakopane – na pokazy róg, graty won"
print(palindrom(s_7_1))


#8. Napisz funkcję, która zwróci
#wszystkie liczby od 1 do n w jednym stringu rozdzielone przecinkami, 
#jednak jeżeli liczba jest podzielna przez:
#trzy – zamiast liczby mamy „Fizz”,
#pięć – zamiast liczby mamy „Buzz”,
#trzy i pięć zamiast liczby mamy „FizzBuzz”.
#wszystkie liczby/słowa mają zostać zwróćone w jednej linii, oraz być rozdzielone przecinkiem
#BEZ spacji
#2 pkt

def fizzbuzz(n):
    numberList = []
    for num in range(0, n+1):
        if num % 3 == 0 and num % 5 == 0 and num != 0:
            num = "FizzBuzz"
            numberList.append(num)
            continue
        elif num % 5 == 0 and num != 0:
            num = "Buzz"
            numberList.append(num)
            continue
        elif num % 3 == 0 and num != 0:
            num = "Fizz"
            numberList.append(num)
            continue
        else:
            numberList.append(num)
            continue
    return numberList

n_8 = 16
print(fizzbuzz(n_8))

#9. Napisz funkcję zwracającą n-ty element ciągu Fibonacciego
# przy F(0)= 0 i F(1) = 1.
#bez rekurencji:
#3 pkt

n_9 = 6

def fibonacci(n):
    element0 = 0
    element1 = 1
    elementyDodawania = []
    elementyDodawania.append(element0)
    elementyDodawania.append(element1)
    sum = 0;
    for i in range(n):
        sum = elementyDodawania[0] + elementyDodawania[1]
        elementyDodawania.remove(elementyDodawania[0])
        elementyDodawania.append(sum)
    return f"Suma {n} elementu = {sum}"
print(fibonacci(n_9))

#10. Napisz funkcję, która dla podanej posortowanej listy
#zwróci index wyszukiwanego elementu za pomocą wyszkukiwania binarnego,
#lub zwróci None gdy nie ma elementu w liscie:
#3 pkt


def binary_search(lista, e):
    rightElement = len(lista) - 1
    leftElement = 0

    while leftElement < rightElement:
        mid = (leftElement + rightElement) // 2
        if lista[mid] > e:
            rightElement = mid - 1
        elif lista[mid] < e:
            leftElement = mid + 1
        else:
            return mid



l_10 = [0,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
print(binary_search(l_10, 2))


