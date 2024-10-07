import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,

}
#print(operations["*"](4,8))

def calculator():
    print(art.logo)
    n1 = float((input("What is the first number?: ")))
    print("+") # For symbol in operations
    print("-") # Print symbol
    print("*")
    print("/")
    operation = input("Pick an operation: ")
    n2 = float(input("What is the next number?: "))
    calculation = operations[f"{operation}"](n1,n2)
    print(f"{n1} {operation} {n2} = {calculation}")
    cont = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation: ").lower()
    while cont == "y":
        n1 = calculation
        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        n2 = float(input("What is the next number?: "))
        calculation = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {calculation}")
        cont = input(f"Type 'y' to continue calculating with {calculation}, or type 'n' to start a new calculation: ").lower()
    calculator()
calculator()

