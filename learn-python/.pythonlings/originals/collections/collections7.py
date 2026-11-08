# Exercise: Collections 7
# I AM NOT DONE
#
# A `deque` (say "deck") is a double-ended queue. You can add and remove at
# BOTH ends, and it's very quick at it, even with a huge number of items.
# (A list is slow at changing its front.)
#
#     d.append(x)       add to the right      d.pop()       remove from the right
#     d.appendleft(x)   add to the left       d.popleft()   remove from the left
#
# Starting with the empty deque `d`, do these in order:
#     1. appendleft(1)   2. append(2)   3. appendleft(0)
# Then save d.pop() in `right_val` and d.popleft() in `left_val`.

from collections import deque

d = deque()
???
right_val = ???
left_val = ???
