class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("miau!")
