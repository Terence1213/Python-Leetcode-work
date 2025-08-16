from abc import ABC, abstractmethod

class Student:
    students_count = 0 # This is class variable (basically static variable), where the variable isn't unique to each instance. 

    def __init__(self, name: str, surname: str, course: str, age: int):
        self.name = name
        self.surname = surname
        self.course = course
        self.age = age
        Student.students_count += 1 # Every time a new student is created, the class variable students_count is incremented by 1

my_student = Student("Terence", "Portelli", "Computer Science", 17)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating!")

class Mammal:
    def give_info():
        print("I am a mammal!")
        
class Dog(Animal, Mammal):
    def bark(self):
        print("WOOF!")

dog = Dog("Browni")
dog.eat()
dog.bark()
dog.give_info()

# Note that there can be multi level inheritance, meaning that a child can have a grand parent technically, or even having more than one parent.

# With constructors, in the child class, if we want to add a new property we have to rewrite the constructor completely with the super keyword.
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"Color: {self.color}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
    
    def describe(self):
        super().describe()
        print(f"Radius: {self.radius}")

circle = Circle("red", True, 5)

class Literature:
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def read_book():
        pass

class Book(Literature):
    def read_book():
        print("Reading a literature book!")

book = Book()
book.read_book()

class Student:
    count = 0

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    def __init__(self, width, height):
        self._width = width # The underscore makes it so the variable is private
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @height.setter 
    def width(self, width):
        self._width = width
    
