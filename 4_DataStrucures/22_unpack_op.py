# numbers = [1, 2, 3]
# print(numbers)
# print(1, 2, 3)

# numbers = [1, 2, 3]
# print(*numbers)
# print(1, 2, 3)

values = list(range(5))
# *range(5)  # We can unpack any iterable
values = [*range(5), *"Hello"]
print(values)


first = [1, 2]
second = [3]
values = [*first, "a", *second, "b"]

# dictionaries

first = {"x:1"}
second = {"x": 10, "y": 2}
# if you have multiple values, the last value will be used
combined = {**first, **second, "z": 1}
print(combined)
