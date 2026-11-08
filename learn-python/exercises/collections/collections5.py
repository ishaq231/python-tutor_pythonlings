# Exercise: Collections 5
# I AM NOT DONE
#
# A `namedtuple` is a tuple whose positions have names. This is easier to read
# than remembering that item [0] is x. You first make the type, giving it a name
# and the names of its fields:
#
#     Pet = namedtuple("Pet", ["name", "age"])
#     rex = Pet("Rex", 3)
#     rex.name         gives   "Rex"
#
# Make `Point` a namedtuple type with the fields x and y, then make `p` a
# Point with x=3 and y=4.

from collections import namedtuple

Point = ???
p = ???
