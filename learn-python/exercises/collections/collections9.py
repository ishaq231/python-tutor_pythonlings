# Exercise: Collections 9
# I AM NOT DONE
#
# Counters can do maths! Adding two counters adds up the counts of each item.
# Subtracting takes the counts away, and drops anything that falls to zero or
# below.
#
#     Counter(a=2) + Counter(a=1, b=1)     gives   Counter({"a": 3, "b": 1})
#
# Two days of shop stock are given.
# 1. `combined` is `monday` plus `tuesday`.
# 2. `remainder` is `combined` minus `sold`.

from collections import Counter

monday  = Counter({"apple": 5, "banana": 3, "cherry": 2})
tuesday = Counter({"apple": 2, "banana": 4, "date": 1})
sold    = Counter({"apple": 4, "banana": 5, "cherry": 1})

combined  = ???
remainder = ???
