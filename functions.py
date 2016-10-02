#!/usr/bin/python3

def main():
    for n in range(1, 20):
        isPrime(n)

    optionalArguments(20, 1440)
    arbitaryNumberOfArguments(1, 2, 3, 4, 5, 6)
    print(returnString())

    for i in inclusiveRange(25):
        print(i, end=' ')

def isPrime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n//x))
            return False
        else:
            print(n, "is a prime number")
            return True

#pass is legal content that doesn't do anything. Use it to make a stub.
def emptyFunction():
    pass

#Optional arguments can be given by giving default values
def optionalArguments(number, second = 202, third = 101):
    print(number, second, third)

#Creates a tuple for the remaining values. ** to create a dictionary.
def arbitaryNumberOfArguments(first, second, *args):
    print(type(args), args)

def returnString():
    return 'String returned from here'

def inclusiveRange(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError("requires at least one argument")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError("inclusive range expects at most 3 arguments")
    i = start
    while i <= stop:
        yield i # This returns i, but the execution will happen right after where the yield happened. The execution
        # continues right after the yield.
        i += step

if __name__ == "__main__": main()
