# Simple CLI Calculator - Version 2.0 (Bug Fixed & Improved)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Fix for Bug TC_CALC_06
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def get_number(prompt):
    # Fix for Bug TC_CALC_08
    while True:
        val = input(prompt)
        try:
            return float(val)
        except ValueError:
            print("Error: Invalid number format. Please enter a valid number.")

def run_calculator():
    print("=== Simple CLI Calculator (v2.0 - Stable) ===")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1-4): ")
    if choice not in ['1', '2', '3', '4']:
        print("Invalid Operation Selected")
        return

    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")

if __name__ == "__main__":
    run_calculator()
