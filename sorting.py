# Sorting - Ascending Order Default
arr = [5, 4, 7, 3, 8]
arr.sort()
print(arr)

# Descending
arr.sort(reverse=True)
print(arr)

# Sorts in alphabetical order
arr = ['bob', 'alice', 'jane', 'doe']
arr.sort()
print(arr)

# Custom sort (by length of string)
# Lamba: Function without a name
arr.sort(key=lambda x: len(x))
print(arr)
