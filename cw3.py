moja_lista = ["Warszawa", "Kraków", "Wrocław",
              "Łódź", "Poznań", "Gdańsk", "Szczecin",
              "Bydgoszcz", "Lublin", "Białystok"]

for element in moja_lista:
    element = "brak"

print(moja_lista)

for i in range(0, len(moja_lista)):
    print(moja_lista[i])

moja_lista[i] = "Lublin"
print(moja_lista)

moja_lista.append("Ostrolenka")
print(moja_lista)

moja_lista.insert(0, "Bialolenka")
print(moja_lista)

print(moja_lista[-3])

moja_lista.extend(["Nowe", "Nowe"])
print(moja_lista)

del moja_lista[0]
print(moja_lista)

moja_lista.append("Gora")
print(moja_lista.pop())

print(moja_lista.pop(0))

index = moja_lista.index("Nowe")
print(index)
print(moja_lista.pop(index))