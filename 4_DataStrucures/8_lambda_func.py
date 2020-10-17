items = [
    ("Item1", 10),
    ("Item2", 9),
    ("Item3", 12),
]


# def sort_item(item):
#     item[1]


# items.sort(key=lambda parameters: expression)
# Shorter way to define function that will be used once
items.sort(key=lambda item: item[1])
print(items)
