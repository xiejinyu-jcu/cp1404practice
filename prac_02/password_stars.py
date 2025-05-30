MIN_LENGTH = 8


def main():
    """Main program to get the password and show the asterisk """
    password=get_password(MIN_LENGTH)
    asterisk=("*"*len(password))
    print(f"your Pythonista is {asterisk} ")


def get_password(min_length):
    """ get the password and compare with the minimum length """
    password=input("Enter the password: ")
    if len(password)>=MIN_LENGTH:
        return password
    print("The password must be at least 8 characters ")
    return get_password(min_length)

main()