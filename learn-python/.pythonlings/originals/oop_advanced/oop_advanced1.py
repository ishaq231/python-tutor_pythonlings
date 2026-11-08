# Exercise: Oop Advanced 1
# I AM NOT DONE
#
# Time to level up your classes! INHERITANCE lets one class (the CHILD) get
# everything from another class (the PARENT). You put the parent's name in
# brackets after the child's name:
#
#     class Puppy(Dog):
#         pass
#
# Puppy automatically has all of Dog's attributes and methods. A child is a
# special kind of its parent, so we say "a Puppy IS A Dog".
#
# Replace the ??? so that `Dog` inherits from `Animal`. A Dog should then
# be able to speak() without you writing any more code.

class Animal:
    def speak(self):
        return "sound"

class Dog(???):
    pass
