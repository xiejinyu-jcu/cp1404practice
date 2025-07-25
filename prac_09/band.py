from musician import  Musician
class Band:
    """a band class with a list musicians"""
    def __init__(self,name=""):
     """Initialise a Band instance."""
     self.name=name
     self.musicians = []


    def add(self, musician):
     """add a musician to the band."""
     self.musicians.append(musician)

    def __str__(self):
        """return a string  of the band and musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
     """return a string for each musician with their corresponding instrument"""
     return "\n".join(musician.play() for musician in self.musicians)



