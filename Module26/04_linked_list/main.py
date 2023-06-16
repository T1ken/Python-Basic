import collections
lst = collections.deque()

# Inserting elements at the front
# or back takes O(1) time:
lst.append('B')
lst.append('C')
lst.appendleft('A')

