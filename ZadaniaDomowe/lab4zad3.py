#Zestaw 3. Napisz funkcję szyfrującą wiadomość szyfrem cezara.
# Dla ułatwienia należy przekształcić wiadomość tak aby zawierała tylko wielkie lub małe litery.
# Funkcja przyjmuje: wiadomość
#– tekst do zaszyfrowania, klucz
#– liczbę o ile należy przesunąć litery w alfabecie oraz zwraca zaszyfrowaną wiadomość w formie łańcucha znaków -string. (40%)
#Funkcja szyfruje tylko litery – inne znaki wstawia do końcowej zaszyfrowanej wiadomości bez zmian(10%)
#Funkcja rozwiązuje problem klucza przesuwającego litery poza zakres listy  z alfabetem oraz problem podania klucza o dowolnej wielkości(20%).
#Funkcja opcjonalnie przyjmuje dowolny alfabet. Domyślnie używa angielskiego(10%).


def szyfruj(text, key):
        coded = " "
        for letter in range(len(text)):
            if text[letter].isalpha():
                if ord(text[letter]) < 122 - key:
                    coded += chr(ord(text[letter]) + key)
                else:
                    coded += chr(ord(text[letter]) + key - 26)
            else:
                coded += text[letter]
        return coded



text = input("Enter what you want to encode: ")
print(f"Encoded: {szyfruj(text, 7)}" )

