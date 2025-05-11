def display_menu():
    print("\n--- String Set Operations Using Array (ADT) ---")
    print("1. Insert String")
    print("2. Search String")
    print("3. Delete String")
    print("4. Find Minimum (Alphabetically)")
    print("5. Find Maximum (Alphabetically)")
    print("6. Find Successor")
    print("7. Find Predecessor")
    print("8. Display All Strings")
    print("9. Exit")

def insert_string(data):
    s = input("Enter string to insert: ").strip()
    if not s:
        print("Invalid input. String cannot be empty.")
        return
    if s in data:
        print("String already exists.")
    else:
        data.append(s)
        print(f"Inserted: '{s}'")

def search_string(data):
    s = input("Enter string to search: ").strip()
    if not s:
        print("Invalid input.")
        return
    if s in data:
        print(f"Found: '{s}'")
    else:
        print("String not found.")

def delete_string(data):
    s = input("Enter string to delete: ").strip()
    if not s:
        print("Invalid input.")
        return
    if s in data:
        data.remove(s)
        print(f"Deleted: '{s}'")
    else:
        print("String not found.")

def find_min(data):
    if not data:
        print("No strings stored.")
        return
    min_val = min(data)
    print(f"Minimum (Alphabetically): '{min_val}'")

def find_max(data):
    if not data:
        print("No strings stored.")
        return
    max_val = max(data)
    print(f"Maximum (Alphabetically): '{max_val}'")

def find_successor(data):
    s = input("Enter string to find successor: ").strip()
    if not s:
        print("Invalid input.")
        return
    if s not in data:
        print("String not found.")
        return
    sorted_data = sorted(data)
    index = sorted_data.index(s)
    if index + 1 < len(sorted_data):
        print(f"Successor of '{s}' is '{sorted_data[index + 1]}'")
    else:
        print("No successor.")

def find_predecessor(data):
    s = input("Enter string to find predecessor: ").strip()
    if not s:
        print("Invalid input.")
        return
    if s not in data:
        print("String not found.")
        return
    sorted_data = sorted(data)
    index = sorted_data.index(s)
    if index > 0:
        print(f"Predecessor of '{s}' is '{sorted_data[index - 1]}'")
    else:
        print("No predecessor.")

def display_all(data):
    if not data:
        print("No strings stored.")
        return
    print("All Strings (sorted):")
    for s in sorted(data):
        print(f"'{s}'")

def main():
    data = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        if choice == '1':
            insert_string(data)
        elif choice == '2':
            search_string(data)
        elif choice == '3':
            delete_string(data)
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
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()
