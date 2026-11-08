# Exercise: Oop Advanced 2
# I AM NOT DONE
#
# A child class often needs its own __init__ as well. But then the parent's
# __init__ doesn't run by itself! `super()` means "my parent class". Use it to
# call the parent's method:
#
#     super().__init__(name)
#
# That sets up the parts that the parent looks after, so you don't repeat
# yourself, and then the child adds its own bits.
#
# Replace the ??? so that `Employee` runs `Person`'s __init__ with the name.

class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, role):
        ???
        self.role = role
