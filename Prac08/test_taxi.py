"""
CP1404/CP5632 Practical
Client code to use the Taxi class
"""
from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi


def main():
    prius = Taxi("Prius 1", 100)

    prius.drive(40)     #drive 40km and print
    print (prius)

    prius.start_fare()  #restart the meter and drive 100km
    prius.drive(100)
    print(prius)

    ucar = UnreliableCar("SuperReliable",90,50.0)
    ucar.drive(40)
    print(ucar)

    silverTaxi = SilverServiceTaxi("Silver Service Taxi",100)
    silverTaxi.drive(50)
    print (silverTaxi)

main()