from unreliable_car import  UnreliableCar

def unreliable_car_test():
    """test the unreliable car class"""
    car=UnreliableCar("example car",100, reliability=30)
    successful_drives = 0
    attempts_drives = 100
    for i in range(attempts_drives):
          distance=car.drive(1)
          if distance > 0:
             successful_drives += 1
    print(f"Successful drives: {successful_drives} out of {attempts_drives}")

unreliable_car_test()