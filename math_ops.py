# math_operations.py

def divide_numbers(a, b):
    """Divides two numbers and returns the result."""
    if b == 0:
        print("Cannot divide by 0")
    else:
        return a / b  

def ultimate_function():
    print("I am the ultimate function! Haha! Prepare!")
    print("No one is superior to me!")
    print("I am not one... not two... but THREE print statements!")

if __name__ == "__main__":
    x = 10
    y = 0
    result = divide_numbers(x, y)
    print(f"The result of division is: {result}")
    ultimate_function()