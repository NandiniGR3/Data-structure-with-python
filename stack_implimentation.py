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
