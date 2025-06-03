"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting.
(We prefer f-strings in this subject.)
Want to read more about it?
https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# Use f-string formatting to produce the output:
print(f"{year}{name} for about {cost}.")
numbers = [1, 19, 123, 456, -25]


#  Using a for loop with the range function and f-string formatting
for i in range(0,11):
    result=2**i
    print(f"2^{i:2} is {result}")


