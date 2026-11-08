# Exercise: Classes 5
# I AM NOT DONE
#
# Methods can also CHANGE the object's attributes. This one remembers a
# number and goes up each time you use it:
#
#     self.count = self.count + 1        (or  self.count += 1)
#
# Replace `pass` in `increment` so that it adds 1 to `self.count`.

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        pass


c = Counter()
c.increment()
c.increment()
c.increment()
