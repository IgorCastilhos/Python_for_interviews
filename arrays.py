# Arrays (called lists in Python)
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

# O(n)
arr.insert(1, 7)
print(arr)

# O(1)
arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# CAREFUL. -1 is not out of bounds,
# it's the last value
arr = [1, 2, 3]
print(arr[-1])

# Indexing -2 is the second to last value, etc.
print(arr[-2])

# Sublist (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:])

# Unpacking
a, b, c = [1, 2, 3]
print(a, b, c)

# Loop through arrays
nums = [1, 2, 3]

# Using index
for i in range(len(nums)):
    print(i, nums[i])

for i, n in enumerate(nums):
    print(i, n)

# Without index
for n in nums:
    print(n)

# Loop through multiple arrays simultaneously
# with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)

# Reverse
nums = [1, 2, 3]
nums.reverse()
print(nums)
