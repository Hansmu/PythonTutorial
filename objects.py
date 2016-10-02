#!/usr/bin/python3

class Egg:
    def __init__(self, kind = "fried"): #constructor
        self.kind = kind

    def whatKind(self):
        return self.kind

class Animal:
    def talk(self): print("I have something to say!")
    def walk(self): print("Hey! I'm walking here!")

class Duck(Animal): #Inherits
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'white')

    def quack(self):
        print("Quaaaack!")

    def walk(self):
        super().walk()
        print("Walks like a duck.")

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    fried = Egg()# Create object
    scrambled = Egg("scrambled")
    print(fried.whatKind())#Self passed implicitly with the dot
    print(scrambled.whatKind())

    donald = Duck()
    donald.walk()

    #Instead of interface make a tuple, then iterate over it and call the method
    for o in (donald, donald):
        o.walk()

if __name__ == "__main__": main()