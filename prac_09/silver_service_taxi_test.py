from silver_service_taxi import SilverServiceTaxi

def test_silver_taxi():
    """ test the silver taxi class"""
    taxi=SilverServiceTaxi("Lexus", 100, fanciness=1)
    taxi.start_fare()
    taxi.drive(10)
    fare = taxi.get_fare()
    print(f"Fare for {taxi.name} is the  ${fare:.2f}")
    print(taxi)


test_silver_taxi()