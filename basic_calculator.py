def get_input():
    try:
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        return x, y
    except ValueError:
        print("Invalid input! Please enter integers only.")
        return get_input()

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed!"
    return x / y

x, y = get_input()

print(f"The sum is {add(x, y)}")
print(f"The difference is {subtract(x, y)}")
print(f"The product is {multiply(x, y)}")
print(f"The quotient is {divide(x, y)}")
