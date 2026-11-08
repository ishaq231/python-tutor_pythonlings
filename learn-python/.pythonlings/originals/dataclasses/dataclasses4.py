# Exercise: Dataclasses 4
# I AM NOT DONE
#
# Careful! A default of `[]` (an empty list) is dangerous: it would be ONE list
# shared by every object, so adding to one basket changes all the others. Python
# stops you from doing this.
#
# The safe way is `default_factory`, which makes a brand new list for each
# object:
#
#     from dataclasses import field
#     items: list = field(default_factory=list)
#
# Fix the `items` field in `Basket` that way (and import `field`).

from dataclasses import dataclass


@dataclass
class Basket:
    label: str
    items: list = []  # Bug: mutable default — use field(default_factory=list)


b1 = Basket("fruit")
b2 = Basket("veggies")
b1.items.append("apple")
