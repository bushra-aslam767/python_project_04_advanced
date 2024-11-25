def main():
    # Create a list called fruit_list that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the original list
    print("Original list of fruits:", fruit_list)

    # Add a new fruit, 'mango', to the list
    fruit_list.append('mango')
    print("After adding 'mango':", fruit_list)

    # Remove 'grape' from the list
    fruit_list.remove('grape')
    print("After removing 'grape':", fruit_list)

    # Check if 'banana' is in the list
    if 'banana' in fruit_list:
        print("'banana' is in the fruit list!")

    # Find the index of 'orange'
    orange_index = fruit_list.index('orange')
    print("The index of 'orange' is:", orange_index)

    # Sort the list in alphabetical order
    fruit_list.sort()
    print("Sorted list:", fruit_list)

    # Reverse the list
    fruit_list.reverse()
    print("Reversed list:", fruit_list)

    # Print the length of the list
    print("The number of fruits in the list:", len(fruit_list))

if __name__ == "__main__":
    main()
