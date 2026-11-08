# Exercise: Collections 8
# I AM NOT DONE
#
# A queue is like a line at a shop: first in, first out (FIFO). With a deque,
# you join the line with .append() and the person at the front leaves with
# .popleft().
#
# Pretend it's a printer queue. Add the jobs "doc1", "doc2" and "doc3" to
# `queue` in that order. Then take them off the front one by one into `first`,
# `second` and `third`.

from collections import deque

queue = deque()

# enqueue three jobs
???

# dequeue in FIFO order
first = ???
second = ???
third = ???
