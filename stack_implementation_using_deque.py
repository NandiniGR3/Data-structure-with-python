from collections import deque

def push(stack, item):
    stack.append(item)
    print(f"'{item}' pushed onto the stack.")

def pop(stack):
    if not stack:
        print("Stack Underflow! Cannot pop from an empty stack.")
    else:
        item = stack.pop()
        print(f"'{item}' popped from the stack.")

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
        print("\n--- Stack Menu (deque) ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

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
            print("Invalid input! Please choose 1 to 4.")

if __name__ == "__main__":
    main()
