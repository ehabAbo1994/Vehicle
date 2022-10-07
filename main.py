class Vehicle:
    # Class attribute
    color = "white"

    # initializing Vehicle class
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    # a method to set the seating capacity
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    # a method to set the color
    def Color(self, color):
        return f"the color of the vehicle is {color}"

    # a method to set how much it will cost to repair the vehicle
    def fare(self):
        return self.mileage * 100


# bus class inherits from vehicle class
class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity)

    # overriding the fare method in the vehicle class
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount


# car class inherits from vehicle
class Car(Vehicle):
    def seating_capacity(self, capacity):
        return super().seating_capacity(capacity)

    # overriding the color method in vehicle
    def Color(self, color):
        return super().Color(color)

    # overriding the fare method in vehicle
    def fare(self):
        amount = super().fare()
        amount += amount * 5 / 100
        return amount


# the test of the program
if __name__ == '__main__':
    seat = Vehicle("seat", 240, 18)
    print("Vehicle Name:", seat.name, "Speed:", seat.max_speed, "Mileage:", seat.mileage)
    print(seat.name, seat.max_speed, seat.mileage)
    School_bus = Bus("school bus", 180, 12)
    print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
    print(School_bus.seating_capacity(50))
    audi = Car("audi", 280, 23)
    print(audi.seating_capacity(5))
    print(audi.Color(audi.color))
    print(audi.Color("black"))
    print(audi.fare())
    print(School_bus.fare())
    print(type(School_bus))
    print(type(audi))
    print(isinstance(School_bus, Vehicle))
