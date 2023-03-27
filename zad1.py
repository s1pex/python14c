a = "Python 2023"
b = a
c = a

#1
print(a == b)
print(b == c)

#2
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))

c = "Java 11"
print(a == b)
print(b == c)
print(type(a))
print(type(b))
print(type(c))
print(hex(id(a)), hex(id(b)), hex(id(c)))


def playWithPlayer():
    if len(nickList) == 0:
        player1Nick = input("Player1 enter your nickname: ")
        nickList.append(player1Nick)
        player2Nick = input("Player2 enter your nickname: ")
        nickList.append(player2Nick)

    print(f"Player 1 make a decision :"
            f"1) Rock"
            f"2) Paper"
            f"3) Scissors")
    choise1 = int(input())

    print(f"Player 2 make a decision :"
            f"1) Rock"
            f"2) Paper"
            f"3) Scissors")
    choise2 = int(input())

    if(choise1 == 1 and choise2 == 1):
        result = "Draw"
    elif(choise1 == 2 and choise2 == 2):
        result = "Draw"
    elif(choise1 == 3 and choise2 == 3):
        result = "Draw"
    elif(choise1 == 1 and choise2 == 2):
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


