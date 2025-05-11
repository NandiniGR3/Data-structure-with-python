#method 2
def display_menu():
    print("\n--- Dynamic Set Operations for Complex Numbers ---")
    print("1. Insert Complex Number")
    print("2. Search Complex Number")
    print("3. Delete Complex Number")
    print("4. Find Minimum (by magnitude)")
    print("5. Find Maximum (by magnitude)")
    print("6. Find Successor (by magnitude)")
    print("7. Find Predecessor (by magnitude)")
    print("8. Display All Complex Numbers")
    print("9. Exit")

def insert_complex(data):
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = complex(real, imag)
        if c not in data:
            data.append(c)
            print(f"Inserted {c}")
        else:
            print("Complex number already exists.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def search_complex(data):
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = complex(real, imag)
        if c in data:
            print(f"Found: {c}")
        else:
            print("Complex number not found.")
    except ValueError:
        print("Invalid input.")

def delete_complex(data):
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = complex(real, imag)
        if c in data:
            data.remove(c)
            print(f"Deleted: {c}")
        else:
            print("Complex number not found.")
    except ValueError:
        print("Invalid input.")

def find_min(data):
    if not data:
        print("No records available.")
        return
    min_val = min(data, key=abs)
    print(f"Minimum (by magnitude): {min_val} | Magnitude: {abs(min_val):.2f}")

def find_max(data):
    if not data:
        print("No records available.")
        return
    max_val = max(data, key=abs)
    print(f"Maximum (by magnitude): {max_val} | Magnitude: {abs(max_val):.2f}")

def find_successor(data):
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = complex(real, imag)
        if c not in data:
            print("Complex number not found.")
            return
        sorted_data = sorted(data, key=abs)
        index = sorted_data.index(c)
        if index + 1 < len(sorted_data):
            print(f"Successor of {c} is {sorted_data[index + 1]}")
        else:
            print("No successor.")
    except ValueError:
        print("Invalid input.")

def find_predecessor(data):
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        c = complex(real, imag)
        if c not in data:
            print("Complex number not found.")
            return
        sorted_data = sorted(data, key=abs)
        index = sorted_data.index(c)
        if index > 0:
            print(f"Predecessor of {c} is {sorted_data[index - 1]}")
        else:
            print("No predecessor.")
    except ValueError:
        print("Invalid input.")

def display_all(data):
    if not data:
        print("No complex numbers stored.")
        return
    print("All Complex Numbers (sorted by magnitude):")
    for c in sorted(data, key=abs):
        print(f"{c} | Magnitude: {abs(c):.2f}")

def main():
    data = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        if choice == '1':
            insert_complex(data)
        elif choice == '2':
            search_complex(data)
        elif choice == '3':
            delete_complex(data)
        elif choice == '4':
            find_min(data)
        elif choice == '5':
            find_max(data)
        elif choice == '6':
            find_successor(data)
        elif choice == '7':
            find_predecessor(data)
        elif choice == '8':
            display_all(data)
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
