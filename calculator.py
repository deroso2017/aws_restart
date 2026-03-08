# Calculator
# User Interaction in form of: The user can choose which mathematic operation they want to perform

import re


def calculator(operator, number1, number2):
    if operator == "+":
        return add(number1, number2)
    elif operator == "-":
        return subtract(number1, number2)
    elif operator == "*":
        return multiple(number1, number2)
    elif operator == "/":
        return divide(number1, number2)
    else:
        print("Invalid operator")
        return None


def mainCalc():
    pattern = r"[-+*/]"
    userInputOperator = input(
        "Please select mathematic operation you wants to execute '+ - * /' : "
    )
    if re.match(pattern, userInputOperator) is not None:
        userInputNumber1 = float(input("Enter the first number: "))
        userInputNumber2 = float(input("Enter the second number: "))
        if calculator(userInputOperator, userInputNumber1, userInputNumber2):
            print(
                f"The answer for {userInputNumber1} {userInputOperator} {userInputNumber2} is: ",
                calculator(userInputOperator, userInputNumber1, userInputNumber2),
            )
    else:
        print("invalid operator!! please select a correct operator")
        mainCalc()


def add(number1: float, number2: float):
    result = number1 + number2
    return result


def subtract(number1: float, number2: float):
    result = number1 - number2
    return result


def multiple(number1: float, number2: float):
    result = number1 * number2
    return result


def divide(number1: float, number2: float):
    try:
        result = number1 / number2
        return result

    except ZeroDivisionError:
        print("Divide by 0 not possible; try again")
        mainCalc()


mainCalc()
