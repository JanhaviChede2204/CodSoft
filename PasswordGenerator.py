import random
import string

def gen_pass(len):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(len):
        password += random.choice(characters)

    return password

def main():
    while (True):
        try:
            print("\n----------Password Generator---------\n")
            len = int(input("Enter desired password length: "))

            if len < 0:
                print("Password length cannot be negative.")

            if len==0:
                print("Password length cannot be zero ")
                print("Exiting .....!")
                return

            password = gen_pass(len)
            print("Generated Password:", password)

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
