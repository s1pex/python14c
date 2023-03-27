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

