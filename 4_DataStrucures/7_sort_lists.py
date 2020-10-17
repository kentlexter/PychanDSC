# numbers = [3, 51, 2, 8, 6]
# # numbers.sort(reverse=True)  # Descending
# sorted(numbers)  # Unlike the sort method, this will make a new sorted list in memory
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)

# What if we're dealing with tuples?
items = [
    ("Item1", 10),
    ("Item1", 9),
    ("Item1", 12),
]

# items.sort()
# print(items) # nothing will change, python dosent know how to sort this list


def sort_item(item):
    item[1]


# items.sort(sort_item)
items.sort(key=sorted)
print(items)
