# Key should be immutable (numbers and strings)
# Value can be anything
# point = {"x": 1, "y": 2}  # Line 3 and 4 are the same
point = dict(x=1, y=2)

point["x"] = 10
point["z"] = 20
# print(point["a"]) will return error

if "a" in point:
    print(point["a"])

print(point.get("a"))  # Returns none
print(point.get("a", 0))
del point["x"]
print(point)

# for x in point:
#     print(x)

for key in point:
    print(key, point[key])

for key, value in point.items():  # Same with line 21
    print(key, value)
