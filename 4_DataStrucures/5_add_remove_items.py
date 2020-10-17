letters = ["a", "b", "c"]

# Add (When action is part of an object, it is a method)
letters.append("d")  # Add to end of the list
letters.insert(0, "-")  # Insert on given index

# Remove
letters.pop(0)  # one item by index
letters.remove("b")  # removes first instance
del letters[0:3]  # remove by range
letters.clear  # delete everything

print(letters)
