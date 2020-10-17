items = [
    ("Item1", 10),
    ("Item2", 9),
    ("Item3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
