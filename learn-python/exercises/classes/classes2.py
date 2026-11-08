# Exercise: Classes 2
# I AM NOT DONE
#
# Objects usually need to remember information about themselves. A special
# method called `__init__` (two underscores each side) runs automatically
# every time you make a new instance. It sets the object up.
#
#     class Dog:
#         def __init__(self, name):
#             self.name = name
#
# `self` means "this particular object" and is always the first parameter of
# a method. Writing `self.name = name` stores the value ON the object, as an
# ATTRIBUTE (a variable that belongs to the object). You read it back with
# rex.name
#
# Finish `__init__` so that it stores `name` on the instance as `self.name`.

class Dog:
    def __init__(self, name):
        # store name on the instance
        pass


rex = Dog("Rex")
