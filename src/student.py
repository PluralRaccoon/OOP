class Student:
    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

bob = Student("Bob", 20)
karla = Student("Karla", 25)

print(Student.class_year)
print(Student.num_students)