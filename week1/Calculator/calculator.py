

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: You cannot divide by zero"
    else:
        raise ValueError("Invalid operation")


if __name__ == "__main__":
    try:
        print("-------------Test---------------")
        print(f"Check + operation: {calculator(5, 2, '+')}")
        print(f"Check - operation: {calculator(5, 2, '-')}")
        print(f"Check * operation: {calculator(5, 2, '*')}")
        print(f"Check / operation: {calculator(5, 2, '/')}")
        print(f"Check / operation by zero: {calculator(5, 0, '/')}")
        print(f"Check random operation: {calculator(5, 2, '%')}")
    except ValueError:
        print("Invalid operation")


    print("-------------Your operation---------------")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation: ")

    result = calculator(num1, num2, operation)

    print(f"The result is {result}")