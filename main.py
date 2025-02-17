from calculator_art import CALCULATOR

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def perform(n1):
    calculation = operations[input(f"Choose the operation between {operations.keys()}: ")]
    n2 = input("Choose the second number:")
    result = calculation(float(n1),float(n2))
    return result

def user_input():
    if input("Do you want to keep the result? ").lower() == "y":
        keep_number = True
    else:
        keep_number = False
    return keep_number

def main():
    is_active = True
    
    print(F"{CALCULATOR} \n Welcome to the calculator app by eneam-tech")
    
    while is_active:
        n1 = input("Insert the first number: ")

        result = perform(n1)

        print(f"The result is: {result}")

        keep_number = user_input()
        
        while keep_number == True:
            result = perform(result)

            print(f"The result is: {result}")

            keep_number = user_input()
        
        if keep_number == False:
            if input("Do you want to perform other operations? ").lower() == "n":
                print("Bye!")
                is_active = False


main()