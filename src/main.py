from animal import Dog, Cat
from shapes import Circle, Square, Triangle, Pizza

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
    
################################333

shapes = [Circle(5), Square(4), Triangle(6, 8), Pizza(7, ['cheese', 'pepperoni', 'mushrooms'])]

for shape in shapes:
    print(shape.area())
