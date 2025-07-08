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
    else:
        print("No guitars can be displayed.")


