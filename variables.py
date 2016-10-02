#!/usr/bin/python3

def main():
    numbers()
    strings()
    listsAndTuples()
    dictionary()

def numbers():
    num = 42
    floatNum = num / 9
    integerDivision = num // 9
    roundedNum = round(num / 9, 2)
    modulus = 42 % 9
    print(type(num), num)
    print(type(floatNum), floatNum)
    print(type(integerDivision), integerDivision)
    print(type(roundedNum), roundedNum)
    print(type(modulus), modulus)
    print(type(float(num)))
    print(type(int(floatNum)))

def strings():
    s = "This is a \nstring!"
    stringWithVariable = "This is a {} string!".format(42) # Format is a method of the string object.
    rawString = r"\nNo new line here"
    lineAfterLife = '''\
    line after line of text
    regardless of entering
    '''
    print(type(s), s)
    print(type(rawString), rawString)
    print(type(stringWithVariable), stringWithVariable)
    print(type(lineAfterLife), lineAfterLife)
    print(type(s), s[3:6])

def listsAndTuples():
    x = (1, 2, 3) #Tuple is am immutable object. Can't append or anything
    list = [1, 2, 3]
    list.append(5)
    list.insert(0, 10)
    print(type(x), x)
    print(type(list), list)

def dictionary():
    dictOne = {
        'one': 1,
        'two': 2,
        'three': 3
    }

    dictViaConstructor = dict(
        one = 1,
        two = 'two'
    )

    print(type(dictViaConstructor), dictViaConstructor)
    print(type(dictOne), dictOne)
    print(dictOne.items())
    print(dictOne.keys())

    for key in sorted(dictOne.keys()):
        print(key, dictOne[key])

if __name__ == "__main__": main()
