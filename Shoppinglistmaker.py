# Task 1: Function to add items to the list
def add_item(shopping_list, item):
    """Add an item to the shopping list."""
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")
    else:
        print(f"'{item}' is already in the list.")

# Task 2: Function to remove items from the list
def remove_item(shopping_list, item):
    """Remove an item from the shopping list."""
    try:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    except ValueError:
        print(f"'{item}' not found in the list.")

# Task 3: Function to display the entire list in a formatted way
def display_list(shopping_list):
    """Display the shopping list in a formatted manner."""
    print("\nYour Shopping List:")
    if shopping_list:
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")
    print("\n")

# Main function to coordinate the shopping list operations
def main():
    shopping_list = []  # Initialize an empty shopping list

    # Loop to allow continuous interaction with the user until they decide to quit
    while True:
        # Display options to the user
        print("Choose an option:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Display the list")
        print("4. Quit")

        # Process user input
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                item = input("Enter the item to add: ")
                add_item(shopping_list, item)
            elif choice == 2:
                item = input("Enter the item to remove: ")
                remove_item(shopping_list, item)
            elif choice == 3:
                display_list(shopping_list)
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()

