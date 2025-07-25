from random import choice

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








