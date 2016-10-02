#!/usr/bin/python3

def main():
    a, b = 0, 1  # Initialize values like this

    if a < b:  # Instead of braces you have indentation
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a == b")

    print("foo" if a < b else "bar")
    switch()

def switch():
    choices = dict(
        one = 'first',
        two = 'second',
        three = 'third'
    )
    v = 'three'
    print(choices[v])

if __name__ == "__main__": main()
