class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Function using polymorphism
def animal_sound(animal):
    return animal.speak()

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Using polymorphism to call speak method
print(animal_sound(dog))  # Output: Buddy says Woof!
print(animal_sound(cat))  # Output: Whiskers says Meow!
