# Hashset
mySet = set()

# Insert - O(1)
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

# Unlike a list, there can't be any duplicates in a hash set, but we can
# get the length of the hash set to know how many elements have been inserted
print(len(mySet))

# Search - O(1)
print(1 in mySet)
print(2 in mySet)
print(5 in mySet)

# Remove - O(1)
mySet.remove(2)
print(2 in mySet)

# To initialize the hash set with predefined values, we just pass in a list
print(set([1, 2, 3]))

# But just like with lists we can also do set comprehension and manually
# initialize it with a loop
mySet = {i for i in range(5)}
print(mySet)

# Transforming a list in a