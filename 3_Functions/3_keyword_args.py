# def increment(number, by):
def increment(number, by=1):  # default param, all optional
    return number + by  # parameters should come after required


# print(increment(2, 1))
print(increment(2, by=1))  # Keyword Arg

print(increment(2))  # Keyword Arg
