#method 1 for any type data into stack
from collections import deque

# Set maximum size for the stack
MAX_SIZE = 5

def push(stack, item):
    if len(stack) >= MAX_SIZE:
        print(f"Stack Overflow! Cannot push. Max size is {MAX_SIZE}.")
    else:
        stack.append(item)
        print(f"'{item}' pushed onto the stack.")

def pop(stack):
    try:
        item = stack.pop()
        print(f"'{item}' popped from the stack.")
    except IndexError:
        print("Stack Underflow! Cannot pop from an empty stack.")

def display(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents (top to bottom):")
        for item in reversed(stack):
            print(item)

def main():
    stack = deque()

    while True:
        print("\n--- Stack Menu (deque with Max Size & Error Handling) ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        try:
            if choice == '1':
                item = input("Enter item to push: ")
                push(stack, item)
            elif choice == '2':
                pop(stack)
            elif choice == '3':
                display(stack)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                raise ValueError("Invalid menu choice.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()


#method 2 implementation of stack for specific data type(complex)
from collections import deque

# Maximum size of the stack (optional)
MAX_SIZE = 10

def is_valid_complex(input_str):
    try:
        complex(input_str)  # Try to convert input to complex
        return True
    except ValueError:
        return False

def push(stack, item):
    if len(stack) >= MAX_SIZE:
        print("Stack Overflow! Cannot push more complex numbers.")
    else:
        stack.append(item)
        print(f"{item} pushed onto the stack.")

def pop(stack):
    if not stack:
        print("Stack Underflow! Cannot pop from empty stack.")
    else:
        item = stack.pop()
        print(f"{item} popped from the stack.")

def display(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack of Complex Numbers (Top to Bottom):")
        for num in reversed(stack):
            print(num)

def main():
    stack = deque()

    while True:
        print("\n--- Complex Number Stack Menu ---")
        print("1. Push complex number")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == '1':
            raw_input = input("Enter complex number (e.g., 3+4j): ")
            if is_valid_complex(raw_input):
                num = complex(raw_input)
                push(stack, num)
            else:
                print("Invalid complex number format!")
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            display(stack)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please enter 1 to 4.")

if __name__ == "__main__":
    main()