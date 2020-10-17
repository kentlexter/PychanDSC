items = [
    ("Item1", 10),
    ("Item2", 9),
    ("Item3", 12),
]

# prices = []
# for item in items:  # Lists prices of items
#     prices.append(item[1])

# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)

prices = list(map(lambda item: item[1], items))
print(prices)
