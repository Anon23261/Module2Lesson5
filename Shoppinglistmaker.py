# Task 1: Develop a function for users to add items to a list.
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f'Added {item} to the shopping list.')

# Task 2: Implement a function to remove items from the list.
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed {item} from the shopping list.')
    else:
        print(f'{item} not found in the shopping list.')

# Task 3: Create a function to print the entire list in a formatted manner.
def print_list(shopping_list):
    print("Shopping List:")
    if shopping_list:
        for i, item in enumerate(shopping_list, 1):
            print(f'{i}. {item}')
    else:
        print("The shopping list is empty.")

# Example usage
my_shopping_list = []

add_item(my_shopping_list, "Apples")
add_item(my_shopping_list, "Bread")
remove_item(my_shopping_list, "Bread")
print_list(my_shopping_list)
