def show_menu():
    print("\nSelect the operation you want to perform :")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

def addition():
    try:
        input1 = float(input("Enter first number :"))
        input2 = float(input("Enter second number :"))
        sum=input1+input2
        print("Result Sum = ",sum)
    except ValueError:
        print("Error: Only numbers accepted.")

def subtraction():
    try:
        input1 = float(input("Enter first number :"))
        input2 = float(input("Enter second number :"))
        sub=input1-input2
        print("Result = ",sub)
    except ValueError:
        print("Error: Only numbers accepted.")

def multiplication():
    try:
        input1 = float(input("Enter first number :"))
        input2 = float(input("Enter second number :"))
        multi=input1*input2
        print("Result Product = ",multi)
    except ValueError:
        print("Error: Only numbers accepted.")

def division():
    try:
        input1 = float(input("Enter divident :"))
        input2 = float(input("Enter divisor :"))
        div=input1 / input2
        print("Result Quotient = ",div)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Only numbers accepted.")

def modulus():
    try:
        input1 = float(input("Enter first number :"))
        input2 = float(input("Enter a number :"))
        mod=input1%input2
        print("Result Remainder = ",mod)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Only numbers accepted.")

try:
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            modulus()
        elif choice == "6":
            print("Thank you for using Calculator App!")
            break
        else:
            print("Invalid choice. Please try again.")

except KeyboardInterrupt:
    print("\nExiting Calculator App. Goodbye!")
