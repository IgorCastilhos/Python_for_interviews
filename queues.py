# Queues are double ended queues by default
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

# At this point, our queue isn't much different from a stack
# but the benefit is that we can actually pop from the left of the queue
# and we can do this operation in constant O(1) time, unlike with a stack
queue.popleft()
print(queue)

# Since it's double ended, we can also add values to the left of the queue
# so the one that we popped we can add back to the left side
queue.appendleft(1)
print(queue)

# And also we can choose to pop from the right side if we want to
queue.pop()
print(queue)
