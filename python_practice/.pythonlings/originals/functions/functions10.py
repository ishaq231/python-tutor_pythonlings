# Exercise: Functions 10
# I AM NOT DONE
#
# Finish the function `is_palindrome`. It takes a string and returns True if it
# reads the same forwards and backwards (ignore capital letters), otherwise False.
# Example: is_palindrome("Racecar") gives True
# Example: is_palindrome("hello") gives False
#
# The last line then uses your function to make `palindromes`:
# a list of all the words in `words` that are palindromes.

words = ["racecar", "hello", "level", "world", "madam", "python", "noon"]

def is_palindrome(s):
# Hint: compare s.lower() with the same word backwards (s.lower()[::-1])
    pass

palindromes = [w for w in words if is_palindrome(w)]
