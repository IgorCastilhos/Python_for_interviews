# Strings are similar to lists
s = "abc"
print(s[0:2])

# But they are immutable
# s[0] = "a"

# This creates a new string
s += "def"
# Any time you modify a string, it's considered an O(n) time operation
print(s)

# Valid Strings can be converted to integers
print(int("123") + int("123"))

# And numbers can be converted to string
print(str(123) + str(123))

# ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of string (with an empty string delimitor)
strings = ["ab", "cd", "ed"]
print(" ".join(strings))
