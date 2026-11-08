# Exercise: Collections 10
# I AM NOT DONE
#
# Time to use everything from this topic to analyse some data! `log` is a
# list of (category, response time) pairs, from the requests made to a web
# server.
#
# 1. `grouped`: a defaultdict(list) of the response times for each category.
# 2. `hit_counts`: a Counter of how many requests each category received.
# 3. `top_category`: the name of the most-requested category.
#    (.most_common(1) gives a list like [("api", 5)], so you'll need to dig
#    the name out of it.)
# 4. `avg_times`: a normal dictionary of the average response time for each
#    category: the sum of its times divided by how many there are.

from collections import defaultdict, Counter

log = [
    ("api",    120), ("web",  45), ("api",   95), ("db",  300),
    ("web",     60), ("api", 110), ("db",   280), ("web",  55),
    ("api",     85), ("db",  310), ("web",   50), ("api", 100),
]

grouped = ???
for category, value in log:
    ???

hit_counts = ???

top_category = ???

avg_times = ???
