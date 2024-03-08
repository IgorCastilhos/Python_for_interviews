import heapq

# Heaps are common data structures to find the Min and Max of
# a set of values frequently. Under the hood, in Python they're
# implemented with arrays.
minHeap = []

# To create an empty Heap we just create an empty list and to push values to that heap we use heapq.heappush
# to that minHeap, the value.
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# By default, heaps in Python are Min Heaps. So if you push
# a few more values and then to get the minimum value, it'll always be at index[0].
print(minHeap[0])
# That's just how Heaps are implemented.

# To loop through a heap while the length of the heap is non-zero, we can also
# pop values from the Heap with heapq.heappop from that minHeap, and then print the value just popped.
while len(minHeap):
    print(heapq.heappop(minHeap))
# Since it's a minHeap, we will see printed the values from smallest to largest

# Python doesn't have Max Heaps by default. The workaround is to multiply each value pushed by negative one
# and then after the value is popped we also multiply it by negative one to negate the original negative one.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])  # Prints in descending order

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# If you already have the set  of values that you want to build the Heap from
# you can do it in linear time by calling heapq.heapify(), and while that array
# is not an empty, it will keep printing the values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) # Printed from smallest to largest (asc)
