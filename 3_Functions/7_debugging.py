def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total  # I intentionally placed this btw for demo purposes.


print("Start")
print(multiply(1, 2, 3))
