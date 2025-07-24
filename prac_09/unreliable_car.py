import  random
from car import Car


class UnreliableCar(Car):
    """create the children class inherits from Car class"""
    def __init__(self,name, fuel,reliability):
        """Initializes UnreliableCar instance"""
        super().__init__(name,fuel)
        self.reliability=reliability

    def drive(self, distance):
        """determine the value of random number and the reliability  """
        distance_driven = 0
        if random.uniform(0,100) <= self.reliability:
           return super().drive(distance)
        else:
           return distance_driven

