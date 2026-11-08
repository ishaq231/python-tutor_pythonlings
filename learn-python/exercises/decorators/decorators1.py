# Exercise: Decorators 1
# I AM NOT DONE
#
# Remember that functions are values you can pass around? A function that
# takes another function as input is called a HIGHER-ORDER function. This is
# the key idea behind DECORATORS, which are the topic of the next few exercises.
#
#     def run(func):
#         return func()     <- calls the function that was passed in
#
# Fill in `call_it` so that it calls the `func` it is given, and returns
# whatever that function returns. Notice: you pass the function WITHOUT
# brackets (call_it(say_hello)), and call_it adds the brackets.

def call_it(func):
    pass


def say_hello():
    return "hello"


def give_seven():
    return 7
