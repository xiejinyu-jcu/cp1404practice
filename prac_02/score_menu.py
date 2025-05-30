MENU = """G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""

MIN_SCORE = 0
MAX_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    """ main program ,display the menu and  handle choice"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Current score: {score}")
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_star(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")

def get_valid_score():
    """ get and return the valid score and  compare with the length """
    score = int(input("Enter the valid score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("The score must be between 0 and 100")
        score = int(input("Enter the valid score: "))
    return score


def determine_result(score):
    """Determine grade result based on score """
    if score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"

def show_star(score):
    """Print as many stars as the score value"""
    print("*" * int(score))

main()
