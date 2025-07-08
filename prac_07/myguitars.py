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


