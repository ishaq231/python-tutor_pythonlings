# Exercise: Recursion 8
# I AM NOT DONE
#
# Recursion works brilliantly on TREES. A tree is made up of smaller trees. Here
# each tree is a dictionary with a "value" and a list of "children", which are
# trees too. Real examples: family trees and the folders on your computer.
#
# Fill in the two ???:
#     tree_depth: a tree with no children has depth 1. Otherwise its depth is 1
#                 plus the biggest depth among its children.
#                 (max() of a list of the children's depths.)
#     tree_search: is the target the value here OR anywhere in a child?
#                  (any() is True if at least one item is True.)

def tree_depth(tree):
    if not tree["children"]:
        return 1
    return ???


def tree_search(tree, target):
    if tree["value"] == target:
        return True
    return ???
