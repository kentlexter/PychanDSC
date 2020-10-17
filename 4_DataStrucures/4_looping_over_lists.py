letters = ["a", "b", "c"]
# items = [0, "a"]
items = (0, "a")
index, letter = items
for letter in enumerate(letters):
    print(letter)
    print(letter[0], letter[1])

# Code v2
# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(index, letter)
#
