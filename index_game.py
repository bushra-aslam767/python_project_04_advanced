def access_element(lst, index):
    """Access an element at a specific index."""
    try:
        return f"The element at index {index} is: {lst[index]}"
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modify the element at a specific index with a new value."""
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced element {old_value} at index {index} with {new_value}. Updated list: {lst}"
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    """Slice the list between start and end indices."""
    try:
        sliced = lst[start:end]
        return f"Sliced list from index {start} to {end} (exclusive): {sliced}"
    except IndexError:
        return "Indices out of range."

def main():
    # Initialize the list
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]
    print("Welcome to the Index Game!")
    print(f"Here is your initial list: {my_list}")
    print("\nOperations:\n1. Access an element\n2. Modify an element\n3. Slice the list\n4. Exit")
    
    while True:
        try:
            # User selects an operation
            choice = int(input("\nSelect an operation (1/2/3/4): "))
            if choice == 4:
                print("Thanks for playing! Goodbye!")
                break

            if choice == 1:  # Access an element
                index = int(input("Enter the index to access: "))
                print(access_element(my_list, index))
            elif choice == 2:  # Modify an element
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
            elif choice == 3:  # Slice the list
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                print(slice_list(my_list, start, end))
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
