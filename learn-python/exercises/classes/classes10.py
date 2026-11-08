# Exercise: Classes 10
# I AM NOT DONE
#
# An attribute set with self inside __init__ belongs to ONE instance. A CLASS
# ATTRIBUTE is written directly in the class and is SHARED by every instance.
# It's perfect for values that are the same for everything, like pi.
#
#     class Circle:
#         pi = 3.14159        <- shared by all circles
#         def __init__(self, radius):
#             self.radius = radius
#
# At the moment `pi = 3.14159` is inside __init__ with no `self.`, so it is just
# a temporary variable that vanishes. Move that line out to class level
# (indented once, directly under `class Circle:`), and take it out of __init__.

class Circle:
    def __init__(self, radius):
        pi = 3.14159        # wrong: local variable, not a class attribute
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2


c1 = Circle(1)
c2 = Circle(5)
