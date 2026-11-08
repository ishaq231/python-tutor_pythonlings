# Exercise: Functions 10
# I AM NOT DONE
#
# Time to put it all together! A PALINDROME is a word that reads the same
# forwards and backwards, like "level".
#
# A reminder of slicing: `s[::-1]` is a slice that walks backwards through the
# whole string, so it gives you the string reversed. The method .lower() makes
# all the letters small, so that "Racecar" and "racecar" count as the same.
#
# Finish `is_palindrome` so it returns True if the word reads the same both
# ways (ignoring capital letters), and False if it doesn't.
#     is_palindrome("Racecar") gives True
#     is_palindrome("hello")   gives False
#
# The last line is already written. It uses your function to pick out the
# palindromes from `words` (it's a quick way to loop and build a list).

words = ["racecar", "hello", "level", "world", "madam", "python", "noon"]

def is_palindrome(s):
    # Hint: compare s.lower() with its reverse (s.lower()[::-1])
    pass

palindromes = [w for w in words if is_palindrome(w)]
