class Person:
    def __init__(self, name, age):
        self._name = name  # Public property (using a single underscore convention)
        self._age = age    # Public property (using a single underscore convention)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer")

# Create a Person object
person = Person("Alice", 25)

# Access and modify public properties
print(f"Name: {person.name}, Age: {person.age}")

person.name = "Bob"
person.age = 30

print(f"Name: {person.name}, Age: {person.age}")
