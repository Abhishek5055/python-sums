class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def start(self):
        return "Starting the vehicle."

    def stop(self):
        return "Stopping the vehicle."

class Car(Vehicle):
    def __init__(self, color, wheels, brand):
        super().__init__(color, wheels)
        self.brand = brand

    def honk(self):
        return "Honking the horn."

# Creating instances of the classes
car = Car("Red", 4, "Toyota")

# Accessing attributes and methods
print(f"Car Color: {car.color}")
print(f"Car Wheels: {car.wheels}")
print(f"Car Brand: {car.brand}")
print(car.start())
print(car.honk())
