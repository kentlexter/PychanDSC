# # Read only list
# point = (1, 2) + (3, 4)
# print(type(point))
# print(point)

# Read only list
point = (1, 2, 3)
print(point[0])
print(point[0:2])
x, y, z = point

if 10 in point:
    print("exists")
