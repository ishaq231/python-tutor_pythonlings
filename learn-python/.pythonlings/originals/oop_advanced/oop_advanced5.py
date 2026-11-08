# Exercise: Oop Advanced 5
# I AM NOT DONE
#
# Special "dunder" methods (the double underscores before and after the name)
# let your classes work with Python's built-in functions. `__len__` is what
# runs when someone calls len() on your object.
#
# Replace the ??? so that len(playlist) is the number of songs.

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return ???
