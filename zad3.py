
pytania = ["1. Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie: ",
           "2. W jakich okolicznościach czytasz książki najczęściej?",
           "3. Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?",
           "4. Po książki w jakiej formie sięgasz najczęściej?",
           "5. Ile książek czytasz średnio w ciągu roku?",
           "6. Jak często średnio czytasz książki?",
           "7. Po jakie gatunki książek sięgasz najczęściej?"]

odpowiedzi = [["a) słuchanie muzyki","b) podróżowanie","c) inne, jakie?"],
              ["a) podczas podróży","b) w ogóle nie czytam","c) inne, jakie?"],
              ["a) chęć poszerzenia wiedzy","b) czytanie to moje hobby","c) inny, jaki?"],
              ["a) papierowej","b) e-booki na tablecie","c) e-booki (książki elektroniczne) na komputerze"],
              ["a) 0","b) 4-10","c) powyżej 10"],
              ["a) codziennie","b) raz w miesiącu","c) raz na pół roku"],
              ["a) romanse","b) naukowe","c) biograficzne"]]

finalOdp = [];

for i in range(0,6) :
    print(pytania[i])
    for j in range(0, 3) :
        print(odpowiedzi[i][j])
    odp = input("Twoja odpowiedz: ")
    if odp == "a":
        finalOdp.append(odpowiedzi[i][0])
    elif odp == "b" :
        finalOdp.append(odpowiedzi[i][1])
    elif odp == "c" and ( i > 2 ) :
        finalOdp.append(odpowiedzi[i][2])
    if odp == "c" and ( i == 0 or i == 1 or i == 2 ) :
        odpOpcionalna = input("Jakie: ")
        finalOdp.append("c) " + odpOpcionalna)


for i in range(0,6) :
    print(pytania[i])
    print(finalOdp[i])


