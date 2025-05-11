# Stack Implementation in Python - Menu Driven Program

def push(stack, item):
    stack.append(item)
    print(f"Item '{item}' pushed onto the stack.")

def pop(stack):
    if not stack:
        print("Stack Underflow! Cannot pop from an empty stack.")
    else:
        item = stack.pop()
        print(f"Item '{item}' popped from the stack.")

def display(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Current Stack:")
        for i in reversed(stack):
            print(i)

def main():
    stack = []
    
    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to push: ")
            push(stack, item)
        elif choice == '2':
            pop(stack)
        elif choice == '3':
            display(stack)
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()










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
