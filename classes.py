class MyClass:
    # Constructor
    # self is like the 'this' keyword in other languages
    def __init__(self, nums):
        # this is creating a variable called nums and assigning it to the nums that were passed in
        # as a parameter to the constructor
        self.nums = nums
        self.size = len(self.nums)  # Create a variable of the size of the parameter

        # self keyword required as param
        def getLength(self):
            return self.size

        # Call a member function from a member function
        def getDoubleLength(self):
            return 2 * self.getLength()
