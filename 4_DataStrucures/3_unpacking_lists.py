numbers = [1, 2, 3, 4, 5, 6]

# first = numbers[0]
# first = numbers[1]
# first = numbers[2]

# first, second = numbers will return error
# first, second, third = numbers

# first, second, *other = numbers
first, *other, last = numbers
print(first)
print(other)


def multiply(*numbers):
    multiply(1, 2, 3, 4, 5)
