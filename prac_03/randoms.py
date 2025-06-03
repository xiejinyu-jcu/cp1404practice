import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

I see it print the "20";
the smallest number is 5 and the largest is 20
"""


"""
What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?


I see it print the 5;
the smallest number is 3 and the largest number is 9; 
Cannot, because it start the 3 and the step is 4 so the net numer is 5 rather than 4
"""



"""
What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

I see it print the 5.109000718307343;
The smallest number is 2.5 and the largest number is 5.5

"""


"""
Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random
print(random.randint(1,100))