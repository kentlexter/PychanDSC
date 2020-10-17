letters = ["a", "b", "c"]

print(letters.index("a"))
# print(letters.index("d"))  # Will return error

# Count
print(letters.count("d"))
# In operator
if "d" in letters:
    print(letters.index("d"))
