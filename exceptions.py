#!/usr/bin/python3

def main():
    try:
        fh = open('non-existant-file.txt') #Else code could also be brought in here.
    except IOError as e:
        print("Could not open file: ", e)
    else:
        for line in fh:
            print(line.strip())

if __name__ == "__main__": main()
