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
