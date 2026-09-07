# list

fruits = ["apple", "banana", "cherry"]
a = fruits
b = ["apple", "banana", "cherry"]

a == b
print(a == b)  # True, because the contents of the lists are the same


print(a is fruits)  # True, because 'a' and 'fruits' refer to the same object in memory