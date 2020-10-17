# def multiply(x, y):
#     return x*y

# def multiply(*numbers):
#     print(numbers)

# def multiply(*numbers):
#     for number in numbers:
#         print(number)

def multiply(*numbers):
    total = 1
    for number in numbers:
        # total = total * number
        total *= number
    return total  # remember to put it outside of the for loop


multiply(2, 3, 4, 5)  # Tuples are read only, iterable
