from sys import getsizeof

# values = (x*2 for x in range(10))  # set of even numbers
# print(values)

# for x in values:
#     print(x)

# values = (x*2 for x in range(100))
values = (x*2 for x in range(1000))
print("gen:", getsizeof(values))

values = [x*2 for x in range(1000)]
print("list:", getsizeof(values))

# print(len(values)) will not work
