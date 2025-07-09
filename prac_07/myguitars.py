"""
CP1404 Practical 07 - my_guitar
Estimate: 35 minutes
Actual:  minutes
"""

from guitar import  Guitar



def load_guitar(filename):
    """read the guitar form the csv file"""
    guitars=[]
    try:
        with open(filename,"r") as file:
                for line in file:
                    name, year, cost = line.strip().split(',')
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
         print(f"the file {filename} didn't find")
    return guitars


def display_guitar(guitars):
    """display all guitar in the list"""
    if guitars:
        name_width = max(len(guitar.name) for guitar in guitars)
        year_width = max(len(str(guitar.year)) for guitar in guitars)
        cost_width = max(len(f"${guitar.cost:,.2f}") for guitar in guitars)
        for guitar in guitars:
            print(f"{guitar.name:<{name_width}} ({guitar.year:<{year_width}}), ${guitar.cost:>{cost_width}}")
    else:
        print("No guitars can be displayed.")

def add_new_guitar(guitars):
    """adding the new guitars name into list"""
    name = input("Name: ").strip()
    while name != "":
     if any(guitar.name == name for guitar in guitars):
        print("Guitar already exists.")
     else:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input,please enter the valid year and cost .")


