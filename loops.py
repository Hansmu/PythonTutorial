#!/usr/bin/python3

def main():
    a, b = 0, 1

    while b < 50:
        print(b)
        a, b = b, a + b
    print("Done!")

    fh = open('lines.txt', 'r')
    for line in fh.readlines():
        print(line, end='')
    print()

    for i in range(5, 10):
        print(i, end=' ')

    print()
    s = "this is a string"
    for c in s:
        if c == 's': continue
        print(c, end='')
    else:
        print("End of loop.")

if __name__ == "__main__": main()
