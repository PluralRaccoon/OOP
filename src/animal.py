class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating something good.")

    def sleep(self):
        print(f"{self.name} is sleeping good.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

class Cat(Animal):
    def lick(self):
        print(f"{self.name} is licking itself.")

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")
