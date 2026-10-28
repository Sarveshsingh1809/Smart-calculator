
def smart_calculator():
    print("==============================")
    print("      SMART CALCULATOR")
    print("==============================")

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (**)")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Thank you for using Smart Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Try again.")
            continue

        try:
            if choice == "6":
                num = float(input("Enter a number: "))

                if num < 0:
                    print("Error: Negative square root not supported.")
                else:
                    print("Result:", num ** 0.5)

            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                elif choice == "2":
                    result = num1 - num2
                elif choice == "3":
                    result = num1 * num2
                elif choice == "4":
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                        continue
                    result = num1 / num2
                elif choice == "5":
                    result = num1 ** num2

                print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers.")


smart_calculator()
