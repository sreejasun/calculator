def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x/y
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'quit' to end the program")
    
    user=input()
    
    if user=="quit":
        break
    elif user in ("add", "sub", "mul", "div"):
        n = float(input("Enter first number: "))
        m = float(input("Enter second number: "))
        
        if user=="add":
            print("Result: ", add(n,m))
        elif user=="sub":
            print("Result: ", subtract(n,m))
        elif user=="mul":
            print("Result: ", multiply(n,m))
        elif user=="div":
            print("Result: ", divide(n,m))
    else:
        print("Invalid input")
