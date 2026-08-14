class Car:
    

    # This is the constructor method that initializes the attributes of the Car class
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    __str__ = lambda self: f"{self.year} {self.color} {self.model} - {'For Sale' if self.for_sale else 'Not For Sale'}"

    def drive(self):
        print("I am driving my car!")

    def stop(self):
        print("I am stopping my car!")