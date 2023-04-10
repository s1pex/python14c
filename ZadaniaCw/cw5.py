users = {}

print(users)

users = {"lukasz": "email@gmail.com",
         "test": "test@gmail.com",
         "admin": "admin@gmail.com",
         "joe": "joe@gmail.com"}

print(users)

user1 = {"name": "lukasz", "email": "email@gmail.com"}
user2 = {"name": "joe", "email": "joe@gmail.com"}
user3 = {"name": "test", "email": "test@gmail.com"}
user4 = {"name": "admin", "email": "admin@gmail.com"}

print(user1)

print(users.get("lukasz"))

print(user1.get("email"))

print(users["lukasz"])

username = "admin"
if username in users:
    print(users[username])

users["alice"] = "alice@gmail.com"
print(users)

for e in users:
    print(e)

for e in users.values():
    print(e)

print(users.items())

for key, value in users.items():
    print("key is: " + key + "; value is: " + value)

user1.update({"password": "haslo"})
print(user1)

if "paswooooord" in user1:
    del user1["paswooooord"]

if "password" in user1:
    del user1["password"]
print(user1)

print(user1.pop("name"))

print(sorted(users))

sortedDict = {}
for key in sorted(users):
    value = users[key]
    sortedDict[key] = value

print(sortedDict)
