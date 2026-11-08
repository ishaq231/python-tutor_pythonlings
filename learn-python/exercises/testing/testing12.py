# Exercise: Testing 12
# I AM NOT DONE
#
# A TEST SUITE is a collection of tests that together check a whole module.
# Write a SEPARATE test function for each job. Then when one fails, the name
# tells you exactly what's broken.
#
# Below are four small text helper functions. Fill in the four test functions
# (replace each `pass`):
#     test_palindrome    at least 3 asserts (one True, one False, and an edge
#                        case such as "")
#     test_word_count    at least 3 asserts (a sentence, one word, and "")
#     test_title_case    at least 2 asserts
#     test_truncate      at least 3 asserts (a short string that stays the same,
#                        a long one that gets cut, and one exactly on the limit)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def word_count(s):
    if not s.strip():
        return 0
    return len(s.split())


def to_title_case(s):
    return s.title()


def truncate(s, max_len):
    return s if len(s) <= max_len else s[:max_len] + "..."


def test_palindrome():
    pass


def test_word_count():
    pass


def test_title_case():
    pass


def test_truncate():
    pass
