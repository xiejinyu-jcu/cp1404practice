import random
MAX_SCORE=100
MIN_SCORE=0
EXCELLENT_SCORE=90
PASSABLE_SCORE=50

def main():
    """ get the user score and print the result"""
    score=float(input("Enter your score: "))
    result=determine_result(score)
    print(result)


def determine_result(score):
    """ determine the grades based the score , return the grade  """
    if score>MAX_SCORE or score <MIN_SCORE:
        return "invalid score"
    elif score>=EXCELLENT_SCORE:
        return"excellent"
    elif score>=PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


random_score=random.randint(0,100)
random_score_result=determine_result(random_score)
print(f"The random score is {random_score} the result is {random_score_result}")

main()