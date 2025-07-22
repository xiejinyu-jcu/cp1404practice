# from the taxi file export to the Taxi class
from taxi import Taxi

# create the new object called my_taxi and setting the argument
my_taxi=Taxi("Prius 1", 100, 1.23)

# driving for 40 km
my_taxi.drive(40)

#print the taxi details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")

# Reset and drive another 100 km
my_taxi.start_fare()
my_taxi.drive(100)

#print the new details and new fare
print(my_taxi)
print(f"Fare: ${my_taxi.get_fare():.2f}")