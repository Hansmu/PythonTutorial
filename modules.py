#!/usr/bin/python3

import sys

def main():
    print("Python version {}.{}.{}".format(*sys.version_info))
    print(sys.platform)

    import os
    print(os.name)
    print(os.getenv('PATH'))

    import random
    print(random.randint(1, 1000))

if __name__ == "__main__": main()
