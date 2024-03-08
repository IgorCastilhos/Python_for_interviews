# Tuples are like lists (arrays) but immutable
tuple1 = (1, 2, 3)
print(tuple1)
# tuple1[0] = 1

# Tuples are mainly used as keys for a hash map or a hash set
# In this case, it is mapping a pair of values (one and two) to three
# This tuple is basically our hashable key
myMap = {(1, 2): 3}

# You can do the same for hash sets
mySet = set()
mySet.add((1, 2))
# And then you can use that tuple to search the hash set
print((1, 2) in mySet)

# The reason we do this is because lists are NOT hashable and can't be keys
# for hash sets or hash maps
# myMap[[3,4]] = 5 <-- This will not work

