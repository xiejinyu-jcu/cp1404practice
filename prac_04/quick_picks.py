import random

MIN_NUMBER=1
MAX_NUMBER=45
NUMBERS_PER_LINE = 6




def main():
    """get the pick number and print the random result"""
    pick_number=int(input("How many quick picks? "))
    for i in range(pick_number):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in quick_pick))



def generate_quick_pick():
    """generate the line and the random number adding to list  """
    numbers=[]
    while len(numbers)< NUMBERS_PER_LINE:
         number=random.randint(MIN_NUMBER,MAX_NUMBER)
         if number not in numbers:
             numbers.append(number)
         numbers.sort()
    return numbers




main()









