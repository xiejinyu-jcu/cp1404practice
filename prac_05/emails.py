"""
email
Estimate: 20 minutes
Actual:   32 minutes
"""



def main():
    email_to_name={}
    email=input("Email: ")
    while email !="":
        user_name=extract_email_name(email)
        confirmation = input(f"Is your name {user_name}? (Y/n) ").lower()
        if confirmation !="Y" and confirmation!="":
           user_name=input("Name: ")
           email_to_name[email]=user_name
           email=input("Email:")
    for email, user_name in  email_to_name.items():
        print(f"{user_name} ({email})")







