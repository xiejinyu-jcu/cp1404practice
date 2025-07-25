

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = 'q)uit, c)hoose taxi, d)rive'


def main():
    """create the main to simulator the taxi """
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_car=None
    total_bill=0.0
    print("Let's drive!")
    print(MENU)
    choice=input("<<< ").lower()


def display_taxis(taxis):
    """display the taxi form the list """
    for i,taxi in enumerate(taxis):
        print(f"{i}-{taxi}")

def choose_taxi(taxis):
    """ accord the user choose,print a list of available taxis"""
    display_taxis(taxis)
    choice=int(input("Choose taxi:"))
    if choice in range(len(taxis)):
        current_taxi=taxis[choice]
    else:
        print("invalid taxi choice")
    print(f"bill to date: ${total_bill:.2f}")
    return current_taxi




