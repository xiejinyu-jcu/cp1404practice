

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """create the main to simulator the taxi """
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_car=None
    bill=0.0
    print("Let's drive!")
    print(MENU)
    choice=input("<<< ").lower()


def display_taxis(taxis):
    """display the taxi form the list """
    for i,taxi in enumerate(taxis):
        print(f"{i}-{taxi}")

def choose_taxi(taxis,current_taxi,bill):
    """ accord the user choose,print a list of available taxis"""
    display_taxis(taxis)
    choice=int(input("Choose taxi:"))
    if choice in range(len(taxis)):
        current_taxi=taxis[choice]
    else:
        print("invalid taxi choice")
    print(f"bill to date: ${bill:.2f}")
    return current_taxi


def drive_taxi(current_taxi,bill):
    """simulate the drive and calculate the fare"""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        current_taxi.start_fare()
        distance=float(input("Drive how far? "))
        current_taxi.drive(distance)
        fare_cost=current_taxi.get_fare()
        print(f"your {current_taxi.name} fare cost is ${fare_cost:.2f}")
        bill+=fare_cost

    print(f"bill to date: ${bill:.2f}")
    return  bill
