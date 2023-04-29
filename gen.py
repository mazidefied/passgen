import random

import string

def generate_password(length, use_lower, use_upper, use_digits, use_special):

    """Generate a random password."""

    chars = ""

    if use_lower:

        chars += string.ascii_lowercase

    if use_upper:

        chars += string.ascii_uppercase

    if use_digits:

        chars += string.digits

    if use_special:

        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))

def generate_passwords(num_passwords, length, use_lower, use_upper, use_digits, use_special):

    """Generate a list of random passwords."""

    passwords = []

    for i in range(num_passwords):

        password = generate_password(length, use_lower, use_upper, use_digits, use_special)

        passwords.append(password)

    return passwords

def save_passwords_to_file(passwords, file_path):

    """Save a list of passwords to a file."""

    with open(file_path, "w") as file:

        for password in passwords:

            file.write(f"{password}n")

if __name__ == "__main__":

    print("**********************************************")

    print("*        Password Generator by Gus            *")

    print("**********************************************n")

    num_passwords = int(input("How many passwords do you want to generate? "))

    length = int(input("What length should the passwords be? "))

    use_lower = input("Use lowercase letters? (y/n) ").lower() == "y"

    use_upper = input("Use uppercase letters? (y/n) ").lower() == "y"

    use_digits = input("Use digits? (y/n) ").lower() == "y"

    use_special = input("Use special characters? (y/n) ").lower() == "y"

    file_path = input("What file path should the passwords be saved to? ")

    passwords = generate_passwords(num_passwords, length, use_lower, use_upper, use_digits, use_special)

    save_passwords_to_file(passwords, file_path)

    print(f"n{num_passwords} passwords have been generated and saved to {file_path}.")

