def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

print("Simple Calculator in Python")
print("---------------------------")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operation +,-,*,/:")


choice = input("Enter choice +,-,/,*  : ")

if choice == '+':
    print("Result:", add(num1, num2))
elif choice == '-':
    print("Result:", subtract(num1, num2))
elif choice == '/':
    print("Result:", multiply(num1, num2))
elif choice == '*':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")
