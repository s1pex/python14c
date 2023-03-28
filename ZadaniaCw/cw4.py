def my_function():
    print("hello world")

my_function()

def my_function_with_argument(name):
    print(f"Hello {name}")

my_function_with_argument("Vladyslav")

def my_function_with_argument(name, surname):
    print(f"Hello {name} {surname}")

my_function_with_argument("Vladyslav", "Raksha")
my_function_with_argument(surname = "Raksha", name = "Vladyslav")

def my_function_with_default(name, surname):
    print(f"Hello \nname: {name}\nsurname: {surname} ")

def my_function_with_opt(name, surname, middle = ''):
    person_data = "name: " + name
    if middle:
        person_data += "\nmiddle name : " + middle
    person_data += "\nsurname : " + surname
    print(f"{person_data}")

print("OPT:")
my_function_with_opt("Lukasz", "Kwasniewicz")
my_function_with_opt("Lukasz", "Kwasniewicz", "Bob")

def my_function_with_return(name, surname, middle = ''):
    person_data = "name: " + name
    if middle:
        person_data += "\nmiddle name : " + middle
    person_data += "\nsurname : " + surname
    return person_data

print("witaj !\n" + my_function_with_return("Lukasz", "Kwasniewicz"))

names = ["Alice", "Bob"]
print(names)

def hello_list(personList):
    for i in range (0, len(personList)):
        personList[i] = "hello" + personList[i]
    hello_list(names)
    print(names)

def hello_multiply(lang, *people):
    greet = ""
    if lang == "PL":
        greet = "Witaj "
    elif lang == "FR":
        greet = "Bonjour"

    for p in people:
        print(greet + p)


hello_multiply("PL", "Alice", "Bob", "Lukasz")






