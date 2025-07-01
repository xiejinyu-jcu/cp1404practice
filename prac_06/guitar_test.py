"""
CP1404 Practical 06 -  Guitar Test
Estimate: 20 minutes
Actual: 17 minutes
"""

from guitar import Guitar

def main():
    """Test the  methods of the Guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)
    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 12. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

main()