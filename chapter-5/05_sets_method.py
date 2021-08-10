b = set()

# # Adding value in empty sets
# b.add(5)
# b.add(6)

# print(b)

# # Important : list can't add into set because that is not hasable ==> change but you can add tuple

# #b.add((2,3,5,67,8))
# print(b)
# print(len(b)) # prints the length of this set
# b.remove(5)
# print(b)

b = b.union({3,5,6,7})
print(b)

# union ----> |
# intersection ----> &
# difference -------> - 