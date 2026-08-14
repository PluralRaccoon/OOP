class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating something good.")

    def sleep(self):
        print(f"{self.name} is sleeping good.")

class Prey(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f"{self.name} is running away from a predator.")

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def hunt(self):
        print(f"{self.name} is hunting for prey.")

class Rabbit(Prey):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating some vegetables.")

class Hawk(Predator):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating a rabbit.")

class Fish(Prey, Predator):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f"{self.name} is eating some algae.")