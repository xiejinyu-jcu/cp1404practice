"""
email
Estimate: 28 minutes
Actual:   40 minutes
"""

def main():
    """make the user input their email address and get their name"""
    email_to_name = {}
    email = input("Email: ").strip()
    while email:
        user_name = extract_email_name(email)
        confirmation = input(f"Is your name {user_name}? (Y/n) ").strip()
        if confirmation.lower() not in ['', 'y']:
            user_name = input("Name: ").strip()
        email_to_name[email] = user_name
        email = input("Email: ").strip()
    for email, user_name in email_to_name.items():
        print(f"{user_name} ({email})")


def extract_email_name(email):
    """ Guess the user's name from the email address  """
    name_part = email.split('@')[0]
    parts = name_part.split('.')
    user_name = ' '.join(part.title() for part in parts)
    return user_name


main()





