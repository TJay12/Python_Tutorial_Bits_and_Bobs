from operator import index
from random import choice

capital = "Auckland"

bird = "Kiwi"

flower = "Daisy"

song = "Nature"

def random_fun_fact():
    funfacts = [
        "funfact one",
        "funfact two!",
        "ff three",
        "ff 4?"
    ]

    index = choice("0123")

    return print(funfacts[int(index)])

# This file will only run in main when called
if __name__ == "__main__":
    random_fun_fact()



