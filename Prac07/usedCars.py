"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from Prac07.car import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))
    limo = Car(100)     #Create a new Car object called “limo” with 100 units of fuel.
    limo.add_fuel(20)   #Add 20 more units of fuel to the car.
    print("Fuel in limo is " + str(limo.fuel) + " litres")  #Display the amount of fuel in the car.
    limo.drive(115) #Attempt to drive the car 115km.
    print("After 115kn, the fuel in limo is " + str(limo.fuel) + " litres")
    print("The limo's odemeter reading is " + str(limo.odometer))    #Display the car’s odometer reading.
main()