# Hasmap (aka dict)
# Just like hashset, we can't have duplicate key inside a hashmap
myMap = {}
myMap["alice"] = 98
myMap["bob"] = 89
print(myMap)
print(len(myMap))

# We can modify the value that's mapped to a key
myMap["alice"] = 12

# Search - O(1)
print("alice" in myMap)

# Remove - O(1)
myMap.pop("alice")
print("alice" in myMap)

# To initialize a hashmap we can add pairs inside the curly braces
myMap = {"alice": 90, "bob": 89}
print(myMap)

# Dict comprehension
# In this case we are mapping i to the value of 2 * i
# This is really powerful for graph problems and to build an adjacency list
myMap = {i: 2 * i for i in range(3)}
print(myMap)

# Looping through a map - Default
myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key, myMap[key])

# We can also directly iterate through the list of values of that hashmap if we don't need the key
for val in myMap.values():
    print(val)

# Using Unpacking we can actually go through the items of that map which will give us the key and the value
for key, val in myMap.items():
    print(key, val)
