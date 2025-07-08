"""
CP1404 Practical 06 - Guitar
Estimate: 20 minutes
Actual: 15 minutes
"""

CURRENT_YEAR=2025
VINTAGE_AGE = 50


class Guitar:
    """create objects and define guitar properties """
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name=name
        self.year = year
        self.cost=cost

    def __str__(self):
        """make the guitar object convert to string """
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """returns how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determine if the guitar is vintage """
        return self.get_age()>=VINTAGE_AGE

    def __lt__(self, other):
        """ Base the year compare the guitar age"""
        return self.year< other.year

