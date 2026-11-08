# Exercise: Oop Advanced 4
# I AM NOT DONE
#
# Programmers use a leading underscore, like `_name`, to signal "this is
# private, please don't touch it directly". A PROPERTY gives controlled access
# to it. The `@property` line above a method lets you use the method like an
# attribute, without the brackets: user.name instead of user.name().
#
# Replace the ??? so the `name` property gives back the private `_name`.

class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return ???
