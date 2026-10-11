# Password Strength Checker

import re

# Checks: length, digit, uppercase, lowercase, special character

def check_password_strength(password):

    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password must contain at least one special character."

    return "Strong: Password meets all the requirements."


def pass_check():
    print("Welcome To The Password Strength Checker")

    while True:
        password = input(
            "Enter a password to check its strength (or type 'exit' to quit): "
        )

        if password.lower() == "exit":
            print("Exiting the Password Strength Checker. Goodbye!")
            break

        strength = check_password_strength(password)
        print(strength)


pass_check()