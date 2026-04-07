print("Hello, world!")
a = 15
b = 12

print("Type of a:", type(a))
print("Type of b:", type(b))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
c = int(a / b)
print("Value of c:", c)
print("Type of c:", type(c))

c = float(c)
print("New value of c:", c)
print("New type of c:", type(c))
message = "The result of a divided by b is "
print(message + str(c))
print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)