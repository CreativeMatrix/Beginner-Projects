from art import logo
from os import system

def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2

def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2):
  return num1 / num2

operations = {
  "+": addition,
  "-": subtraction,
  "*": multiplication,
  "/": division
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    for keys in operations.keys():
        print(keys, end = " ")

    continue_calculation = True
    while continue_calculation == True:
        operation_symbol = input("\nPick an operation: ")
        num2 = float(input("What is the next number?: "))

        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_continue = input(f"Type 'Y' to continue calculating with the answer {answer}, or type 'N' to start a new calculation: ").lower()
        if user_continue == 'y':
            num1 = answer
        elif user_continue == "n":
            continue_calculation = False
            _ = system('cls')
            calculator()
calculator()
