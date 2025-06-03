"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

"""
3.Could you change the code to avoid the possibility of a ?ZeroDivisionError

"""
try:
    numerator = int(input(" Enter the numerator: "))
    denominator = int(input(" Enter the denominator: "))
    while denominator == 0:
          print("invalid number, please try again")
          denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
1.When will a occur? ValueError

In numerator line ,if user input not a valid integer such as the letter or symbols it will occur  
"""

"""
2.When will a occur? ZeroDivisionError

when you processing the fraction , if your denominator is equal to zero it will occur.
"""

