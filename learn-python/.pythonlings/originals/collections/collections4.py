# Exercise: Collections 4
# I AM NOT DONE
#
# A `defaultdict(list)` gives every new key an empty list to start with. That's
# perfect for GROUPING things, because you can append straight away:
#
#     groups = defaultdict(list)
#     groups["fruit"].append("apple")
#
# Group the students by their grade letter. `by_grade` should link each grade to
# a list of the names with that grade, in the original order.

from collections import defaultdict

students = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Carol", "A"),
    ("Dave", "C"),
    ("Eve", "B"),
    ("Frank", "A"),
]

by_grade = ???
for name, grade in students:
    ???
