#3. Napisz grę – papier nożyce kamień. (60%) Gra pozwoli wybrać ilość rund. Pozwoli wybrać tryb gry – komputer / 2 graczy (hot seats) Pozwoli nazwać graczy.
#Zapamięta wynik z każdej rundy. Na koniec wyświetli listę wyników oraz ostateczny wynik z informacją, który gracz wygrał. W opcji hot seats należy użyć getpass
import getpass
import random

gameNum = int(input("Wybierz ilosc rund: "))
print("Tryb gry :")
print("1) Z komputerem")
print("2) 2 gracza")
gameType = int(input("Wybierz tryb gry(1 or 2): "))
nickList = []
gameResult = []

if(gameType == 2):
    for i in range(0, gameNum):
            if len(nickList) == 0:
                player1Nick = input("Player1 enter your nickname: ")
                nickList.append(player1Nick)
                player2Nick = input("Player2 enter your nickname: ")
                nickList.append(player2Nick)

            print(f"Player 1 make a decision :"
                  f" 1) Rock"
                  f" 2) Paper"
                  f" 3) Scissors")
            choise1 = int(input())
            if choise1 == 1:
                symbol1 = "Rock"
            elif choise1 == 2:
                symbol1 = "Paper"
            else:
                symbol1 = "Scissors"

            print(f"Player 2 make a decision :"
                  f" 1) Rock"
                  f" 2) Paper"
                  f" 3) Scissors")
            choise2 = int(input())
            if choise2 == 1:
                symbol2 = "Rock"
            elif choise2 == 2:
                symbol2 = "Paper"
            else:
                symbol2 = "Scissors"

            if (choise1 == 1 and choise2 == 1):
                result = "Draw"
            elif (choise1 == 2 and choise2 == 2):
                result = "Draw"
            elif (choise1 == 3 and choise2 == 3):
                result = "Draw"
            elif (choise1 == 1 and choise2 == 2):
                result = f"{player2Nick} has won"
            elif (choise1 == 1 and choise2 == 3):
                result = f"{player1Nick} has won"
            elif (choise1 == 2 and choise2 == 1):
                result = f"{player1Nick} has won"
            elif (choise1 == 2 and choise2 == 3):
                result = f"{player2Nick} has won"
            elif (choise1 == 3 and choise2 == 1):
                result = f"{player2Nick} has won"
            elif (choise1 == 3 and choise2 == 2):
                result = f"{player1Nick} has won"
            print(result)
            gameResult.append([f"Player {player1Nick} picked {symbol1}, Player {player2Nick} picked {symbol2},result was: {result}"])
    for i in range(len(gameResult)):
        print(gameResult[i])
else:
    for i in range(gameNum):
        if len(nickList) == 0:
            player1Nick = input("Player1 enter your nickname: ")
            nickList.append(player1Nick)

            print(f" Make a decision :"
                  f" 1) Rock"
                  f" 2) Paper"
                  f" 3) Scissors")
            choise1 = int(input())
            if choise1 == 1:
                symbol1 = "Rock"
            elif choise1 == 2:
                symbol1 = "Paper"
            else:
                symbol1 = "Scissors"

            r = random.randrange(0,3)
            if r == 0:
                symbol2 = "Rock"
            elif r == 1:
                symbol2 = "Paper"
            else:
                symbol2 = "Scissors"

            if (choise1 == 1 and r == 0):
                result1 = "Draw"
            elif (choise1 == 2 and r == 1):
                result1 = "Draw"
            elif (choise1 == 3 and r == 2):
                result1 = "Draw"
            elif (choise1 == 1 and r == 1):
                result1 = f"Bot has won"
            elif (choise1 == 1 and r == 2):
                result1 = f"{player1Nick} has won"
            elif (choise1 == 2 and r == 0):
                result1 = f"{player1Nick} has won"
            elif (choise1 == 2 and r == 2):
                result1 = f"Bot has won"
            elif (choise1 == 3 and r == 0):
                result1 = f"Bot has won"
            elif (choise1 == 3 and r == 1):
                result1 = f"{player1Nick} has won"
            print(result1)
            gameResult.append([f"Player {player1Nick} picked {symbol1}, Bot picked {symbol2},result was: {result1}"])
    for i in range(len(gameResult)):
        print(gameResult[i])