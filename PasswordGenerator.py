import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter desired password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        password = generate_password(length)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
