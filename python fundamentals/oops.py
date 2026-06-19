#create a car class with attributes like brand and model . then create an instance of this class

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        

my_car = Car('Toyota','Maruti')
print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")
print(my_new_car.model)

#Add a method to the car class that displays the full name of the car(brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car('Toyota','Maruti')
print(my_car.model)
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)

#create an elctric car class that inherits from the car class and has an additional attribute battery_size.

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

# Create an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", "75 kWh")
print(my_electric_car.full_name())
print(f"Battery Size: {my_electric_car.battery_size}")

#modify the car class to encapsulate the brand attribute , making it private, and provide a geeter method for it.

class Car:
    car_count = 0
    
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.car_count += 1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol/Diesel"
    
    @classmethod
    def get_car_count(cls):
        return cls.car_count
    
    @staticmethod
    def car_description():
        return "A car is a wheeled motor vehicle designed primarily for transportation on roads."

my_car = Car('Toyota','Maruti')
print(my_car.get_brand())
print(my_car.model)
print(my_car.full_name())
print(f"Total cars created: {Car.get_car_count()}")

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(f"Total cars created: {Car.get_car_count()}")

#demonstrate polymorphism by definning a method fuel_type in both car and electric car classes , but diiferent behaviors

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric"

class HybridCar(Car):
    def __init__(self, brand, model, fuel_capacity):
        super().__init__(brand, model)
        self.fuel_capacity = fuel_capacity
    
    def fuel_type(self):
        return "Hybrid (Petrol + Electric)"

# Example 1: Demonstrating polymorphism
print("\n--- Polymorphism Example 1 ---")
car1 = Car("Honda", "Civic")
electric_car = ElectricCar("Tesla", "Model 3", "60 kWh")
hybrid_car = HybridCar("Toyota", "Prius", "50L")

print(f"{car1.full_name()} - Fuel Type: {car1.fuel_type()}")
print(f"{electric_car.full_name()} - Fuel Type: {electric_car.fuel_type()}")
print(f"{hybrid_car.full_name()} - Fuel Type: {hybrid_car.fuel_type()}")

# Example 2: Polymorphism with a list of cars
print("\n--- Polymorphism Example 2 ---")
cars = [
    Car("Maruti", "Swift"),
    ElectricCar("BYD", "Atto 3", "44.9 kWh"),
    Car("Hyundai", "i20"),
    HybridCar("Lexus", "NX 450h", "45L"),
    ElectricCar("Nissan", "Leaf", "62 kWh")
]

print("All cars in the fleet:")
for car in cars:
    print(f"  {car.full_name()} -> {car.fuel_type()}")

#add a static method to the ear class that returns a general description of a car

print("\n--- Static Method Example ---")
# Can call static method on class directly (no instance needed)
print(f"Description: {Car.car_description()}")

# Can also call static method on instance (but not recommended)
my_car_instance = Car("BMW", "X5")
print(f"Description via instance: {my_car_instance.car_description()}")

# Example 2: Using static method in context
print("\n--- Static Method Example 2 ---")
print("General Information:")
print(f"  {Car.car_description()}")
print(f"  Total cars created so far: {Car.get_car_count()}")