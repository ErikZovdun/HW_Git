number1 = float(input("Input number 1: "))
number2 = float(input("Input number 2: "))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operation = input("Choose an operation:\n"
                  "1 - add\n"
                  "2 - subtract\n"
                  "3 - multiplication\n"
                  "4 - division\n")

match operation:
    case "1":
        print("Result: " + add(number1, number2))
    case "2":
        print("Result: " + subtract(number1, number2))
    case "3":
        print("Result: " + multiplication(number1, number2))
    case "4":
        print("Result: " + division(number1, number2))
    case _:
        print("Incorrect operation!")
