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





