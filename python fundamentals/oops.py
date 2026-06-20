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
        self.__model = model
        Car.car_count += 1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        raise AttributeError("Cannot modify model attribute - it is read-only")
    
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

#use a property decorator in the car class to make the model attribute read-only.

print("\n--- Property Decorator Example (Read-Only) ---")
car_readonly = Car("Mercedes", "C-Class")

# Reading the model attribute using property (works fine)
print(f"Car Model (Read): {car_readonly.model}")
print(f"Car Full Name: {car_readonly.full_name()}")

# Trying to modify the model attribute (will raise error)
print("\nAttempting to modify model attribute...")
try:
    car_readonly.model = "E-Class"
except AttributeError as e:
    print(f"Error: {e}")

# Example 2: Multiple cars with read-only model
print("\n--- Property Decorator Example 2 ---")
cars_list = [
    Car("Audi", "A4"),
    Car("BMW", "Series 3"),
    Car("Volvo", "S90")
]

print("Fleet Information (All models are read-only):")
for car in cars_list:
    print(f"  {car.full_name()} - Model: {car.model}")

# Attempting to modify in a loop
print("\nTrying to modify models in loop...")
for car in cars_list:
    try:
        car.model = "Modified Model"
    except AttributeError as e:
        print(f"  Cannot modify {car.full_name()}: {e}")

#Demonstrate the use of isinstance() to check if my_tesla is an instance of car and electric car

print("\n--- isinstance() Example 1 ---")
my_tesla = ElectricCar("Tesla", "Model X", "100 kWh")

# Check if my_tesla is an instance of different classes
print(f"my_tesla is instance of ElectricCar: {isinstance(my_tesla, ElectricCar)}")
print(f"my_tesla is instance of Car: {isinstance(my_tesla, Car)}")
print(f"my_tesla is instance of HybridCar: {isinstance(my_tesla, HybridCar)}")
print(f"my_tesla is instance of str: {isinstance(my_tesla, str)}")

# Example 2: Using isinstance() with multiple object types
print("\n--- isinstance() Example 2 ---")
my_tesla = ElectricCar("Tesla", "Model X", "100 kWh")
regular_car = Car("Maruti", "800")
hybrid_car = HybridCar("Toyota", "Prius", "50L")
battery_size = "100 kWh"

print("Type checking different objects:")
print(f"  my_tesla is ElectricCar? {isinstance(my_tesla, ElectricCar)}")
print(f"  my_tesla is Car (parent)? {isinstance(my_tesla, Car)}")
print(f"  regular_car is Car? {isinstance(regular_car, Car)}")
print(f"  regular_car is ElectricCar? {isinstance(regular_car, ElectricCar)}")
print(f"  hybrid_car is HybridCar? {isinstance(hybrid_car, HybridCar)}")
print(f"  hybrid_car is Car (parent)? {isinstance(hybrid_car, Car)}")
print(f"  battery_size is str? {isinstance(battery_size, str)}")

# Example 3: Using isinstance() in conditional logic
print("\n--- isinstance() Example 3 (Practical Usage) ---")
all_vehicles = [
    Car("Honda", "Civic"),
    ElectricCar("Nissan", "Leaf", "62 kWh"),
    HybridCar("Lexus", "NX", "45L"),
    ElectricCar("BMW", "i3", "42.2 kWh"),
    Car("Hyundai", "Creta")
]

print("Categorizing vehicles:")
for vehicle in all_vehicles:
    if isinstance(vehicle, ElectricCar):
        print(f"  ⚡ {vehicle.full_name()} - Electric (Battery: {vehicle.battery_size})")
    elif isinstance(vehicle, HybridCar):
        print(f"  🔋 {vehicle.full_name()} - Hybrid (Fuel Tank: {vehicle.fuel_capacity})")
    else:
        print(f"  🚗 {vehicle.full_name()} - Regular Car")

#create two classes battery and engine and let the electric car class inherit from both, demonstrating multiple inheritance

# Class 1: Battery
class Battery:
    def __init__(self, capacity, voltage):
        self.capacity = capacity
        self.voltage = voltage
    
    def battery_info(self):
        return f"Battery: {self.capacity}kWh, {self.voltage}V"
    
    def charge(self):
        return "🔌 Battery is charging..."

# Class 2: Engine
class Engine:
    def __init__(self, motor_type, power):
        self.motor_type = motor_type
        self.power = power
    
    def engine_info(self):
        return f"Engine: {self.motor_type} Motor, {self.power}kW"
    
    def start_engine(self):
        return "⚡ Electric motor started!"

# Class 3: ElectricCar inheriting from Car, Battery, and Engine (Multiple Inheritance)
class AdvancedElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_capacity, voltage, motor_type, power):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_capacity, voltage)
        Engine.__init__(self, motor_type, power)
    
    def display_specs(self):
        print(f"Car: {self.full_name()}")
        print(f"  {self.battery_info()}")
        print(f"  {self.engine_info()}")

# Example 1: Simple Multiple Inheritance Demo
print("\n--- Multiple Inheritance Example 1 ---")
tesla = AdvancedElectricCar("Tesla", "Model S", 100, 400, "AC Induction", 325)

print(tesla.full_name())
print(tesla.battery_info())
print(tesla.engine_info())
print(tesla.start_engine())
print(tesla.charge())

# Example 2: Using Multiple Inherited Methods
print("\n--- Multiple Inheritance Example 2 ---")
electric_vehicles = [
    AdvancedElectricCar("Tesla", "Model 3", 75, 400, "Permanent Magnet", 280),
    AdvancedElectricCar("Nissan", "Leaf", 62, 400, "AC Induction", 110),
    AdvancedElectricCar("BMW", "i4", 81.5, 400, "Dual Motor", 380)
]

print("Fleet Specifications:")
for ev in electric_vehicles:
    print(f"\n{ev.full_name()}")
    print(f"  → {ev.battery_info()}")
    print(f"  → {ev.engine_info()}")
    print(f"  → {ev.start_engine()}")
    print(f"  → {ev.charge()}")

# Example 3: Demonstrating MRO (Method Resolution Order)
print("\n--- Multiple Inheritance Example 3 (MRO) ---")
print("Method Resolution Order (MRO) for AdvancedElectricCar:")
print(f"MRO: {[cls.__name__ for cls in AdvancedElectricCar.__mro__]}")

tesla_mro = AdvancedElectricCar("Tesla", "Model X", 100, 400, "Dual Motor", 450)
print(f"\nIsinstance checks:")
print(f"  Is instance of AdvancedElectricCar? {isinstance(tesla_mro, AdvancedElectricCar)}")
print(f"  Is instance of Car? {isinstance(tesla_mro, Car)}")
print(f"  Is instance of Battery? {isinstance(tesla_mro, Battery)}")
print(f"  Is instance of Engine? {isinstance(tesla_mro, Engine)}")