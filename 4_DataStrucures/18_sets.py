# numbers = [1, 1, 2, 3, 4]
# uniques = set(numbers)
# second = {1, 4}
# second.add(5)
# second.remove(5)
# len(second)
# print(uniques)

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 4}

print(first | second)  # union
print(first & second)  # intersection
print(first-second)  # difference
# symmetric difference prints items that are in the first set, but not both
print(first ^ second)

# Unlike lists, sets are unordered. Cannot be accessed by index
# print(first[0]) will return error.

if 1 in first:
    print("yes")
