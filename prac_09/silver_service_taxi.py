from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """create the children class """
    flagfall = 4.50
    def __init__(self,name, fuel,fanciness):
        """Initialize a SilverServiceTaxi instance,inherit the parent class init """
        super().__init__(name,fuel)
        self.price_per_km = Taxi.price_per_km * fanciness


    def __str__(self):
     """Return a string representation of the SilverServiceTaxi  """
     return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

 