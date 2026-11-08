# Exercise: Dictionaries 9
# I AM NOT DONE
#
# A value in a dictionary can be anything, even another dictionary! This
# is a NESTED dictionary. To dig in, use one set of square brackets for each
# level, working from the outside in:
#
#     school["students"]["alice"]["grade"]
#
# Fill in `alice_grade`, `math_room` and `num_students` using `school`.
# The comments in the exercise show you where each answer lives.

school = {
    "students": {
        "alice": {"grade": "A", "age": 20},
        "bob":   {"grade": "B", "age": 22},
    },
    "courses": {
        "math":    {"room": 101, "credits": 3},
        "english": {"room": 205, "credits": 3},
    },
    "meta": {"enrollment": 350, "founded": 1990},
}

alice_grade = ???
math_room = ???
num_students = ???
