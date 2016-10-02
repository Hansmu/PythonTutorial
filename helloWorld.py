#!/usr/bin/python3
# pound sign is a comment indicator. The above line is used for environments that run the script from a shell ex. Linux.
# It should be the first line in scripts.

def main(): # Can collapse the single line function to the same line if you want.
    a, b, c = 1, "one", (1, 2, 3, 4, 5)
    d = [1, 2, 3, 4, 5]
    print(type(a), a)
    print(type(b), b)
    print(type(c), c)
    print(type(d), d)
    print("Hello World!") # Indentation levels have to match on every line

if __name__ == "__main__": main()  # Only runs when the module is called the main module. Won't run when it's included.

#Everything in Python is an object. Variable, functions, even code
#Every object has an ID, type and value
#   ID uniquely identifies a particular instance of an object. It cannot change for the life of the object.
#   Type identifies the class of an object. Cannot change for the life of the object.
#   Value is the content of the object. Mutable objects can change value, immutable cannot.
# Most fundamental types in Python are immutable: numbers, strings and tuples.
# Mutable objects include: lists, dictionaries etc.