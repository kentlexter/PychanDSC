x = 10
y = 11

z = x
x = y
y = z

print("x", x)
print("y", y)

x, y = y, x
x, y = (11, 10)  # defining a tuple, then unpacking it in the left side
a, b = 1, 2
