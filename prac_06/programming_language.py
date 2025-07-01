"""
CP1404 Practical 06 - Programming Language
Estimate: 25 minutes
Actual:  minutes
"""

class ProgrammingLanguage:
    """Represent information about a programming language"""
    def __init__(self,name,typing,reflection,year):
        """Initialize a programming language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine whether the programming language is a dynamically typed language."""
        return self.typing == "Dynamic"

    def __str__(self):
       """make the object convert to string  """
       return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"





