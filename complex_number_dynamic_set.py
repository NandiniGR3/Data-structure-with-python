
def display_menu(): #Defines a function to display a menu of options.
    print("\n--- Dynamic Set Operations for Complex Numbers ---") #Prints a heading to separate the menu visually.
    '''Prints numbered menu options for user interaction.'''
    print("1. Insert Complex Number")
    print("2. Search Complex Number by Key")
    print("3. Delete Complex Number")
    print("4. Find Minimum (by magnitude)")
    print("5. Find Maximum (by magnitude)")
    print("6. Find Successor (by magnitude)")
    print("7. Find Predecessor (by magnitude)")
    print("8. Display All Complex Numbers")
    print("9. Exit")

'''Defines a function to insert a complex number into the data dictionary.'''
def insert_complex(data):
    key = input("Enter unique key (e.g., 'c1'): ").strip() #Takes a unique string key as input and removes leading/trailing spaces.

    if key in data:
        print(" Key already exists.") #Checks for duplicate keys. If found, it exits early.
        return

    try:
        '''Converts input into a complex number using complex(real, imag), stores it in data using the key, and prints confirmation.'''
        real = float(input("Enter real part (a) of complex number (e.g., 3): "))
        imag = float(input("Enter imaginary part (b) (e.g., 4 for '3 + 4j'): "))
        data[key] = complex(real, imag)
        print(f" Inserted {data[key]} with key '{key}'.")
       # print("Current data:", data)  # For debugging
    except ValueError:
        '''Catches errors if the input can't be converted to floats.'''
        print(" Invalid input. Real and imaginary parts must be numbers.")

'''Searches for a key in the dictionary and displays the corresponding complex number if found.'''
def search_complex(data):
    key = input("Enter key to search (e.g., 'c1'): ").strip()
    if key in data:
        print(f" Found: {key} → {data[key]}")
    else:
        print(" Key not found.")

'''Deletes a key from the dictionary if it exists.'''
def delete_complex(data):
    key = input("Enter key to delete (e.g., 'c1'): ").strip()
    if key in data:
        del data[key]
        print(f" Deleted key '{key}'.")
        #print("Current data:", data)  # Shows dictionary after deletion

    else:
        print(" Key not found.")

'''finds the minimum magnitude:'''
def find_min(data):
    if not data:
        print(" No records available.")#Handles the edge case if the dictionary is empty.
        return
    '''Finds the key with the smallest magnitude (absolute value of the complex number).'''
    min_key = min(data, key=lambda k: abs(data[k]))
    print(f"Minimum (by magnitude): {min_key} → {data[min_key]} | Magnitude: {abs(data[min_key]):.2f}")


'''Similar to find_min, but finds the maximum magnitude:'''
def find_max(data):
    if not data:
        print(" No records available.")
        return
    max_key = max(data, key=lambda k: abs(data[k]))
    print(f"Maximum (by magnitude): {max_key} → {data[max_key]} | Magnitude: {abs(data[max_key]):.2f}")


''' looks for the next item in sorted order:'''
def find_successor(data):
    key = input("Enter key to find successor (e.g., 'c1'): ").strip()
    if key not in data:
        print(" Key not found.")
        return
    '''Sorts the keys based on the magnitude of their values.'''
    sorted_keys = sorted(data, key=lambda k: abs(data[k]))
    '''Finds the next key in sorted order by magnitude.'''

    index = sorted_keys.index(key)
    if index + 1 < len(sorted_keys):
        succ_key = sorted_keys[index + 1]
        print(f" Successor of '{key}' is '{succ_key}' → {data[succ_key]}")
    else:
        print(f" No successor for '{key}'.")

'''Same as find_successor, but looks for the previous item in sorted order:'''
def find_predecessor(data):
    key = input("Enter key to find predecessor (e.g., 'c1'): ").strip()
    if key not in data:
        print(" Key not found.")
        return

    sorted_keys = sorted(data, key=lambda k: abs(data[k]))
    index = sorted_keys.index(key)
    if index > 0:
        pred_key = sorted_keys[index - 1]
        print(f" Predecessor of '{key}' is '{pred_key}' → {data[pred_key]}")
    else:
        print(f" No predecessor for '{key}'.")

def display_all(data):
    if not data:
        print(" No complex numbers stored.") #Handles empty dictionary case.
        return
    '''Displays all items sorted by magnitude.'''    
    print(" All Complex Numbers (sorted by magnitude):")
    for key in sorted(data, key=lambda k: abs(data[k])):
        print(f"{key}: {data[key]} | Magnitude: {abs(data[key]):.2f}")

def main():
    '''Initializes an empty dictionary to store complex numbers.'''
    data = {}
    '''Loops through the menu until the user exits.'''
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        '''Handles user input and invokes the appropriate function.'''
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
            print("\nRaw dictionary:", data)
        elif choice == '9':
            print(" Exiting the program.")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 9.")

'''Executes the program when run directly . '''
if __name__ == "__main__":
    main()
