# Nested Functions have access to outer variables.
# These can be really helpful in recursive problems
def outer(a, b):
    c = "c"

    def inner():
        return a + b + c

    return inner()  # inner functions has access to all the outer function variables by default


print(outer("a", "b"))


# Can modify objects but not reassign
# unless using nonlocal keyword

# If we have a function that is going to double every value in an array and also double this value(val) itself
# we can have a helper function. It'll have access to both of those outer variables.
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # We can modify the array pretty easily by going through each value in the array and
        # then doubling it. This works and will update the ORIGINAL array.

        nonlocal val
        val *= 2

    helper()
    print(arr, val)


# If you want to update the value outside the scope of the helper function,
# you'll have to declare it as a nonlocal value and by doing this and then
# modifying the value, it will modify the original values and then in the outer functions we can
# call the helper functions

nums = [1, 2]
val = 3
double(nums, val)
