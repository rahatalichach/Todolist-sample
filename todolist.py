todo_list = []

def add_item(item):
    todo_list.append(item)
    print(f"Item '{item}' added to the todo list")

def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print(f"Item '{item}' removed from the todo list")
        return True
    else:
        print(f"Item '{item}' not found in the todo list")
        return False

def display():
    if len(todo_list) == 0:
        print("Todo list is empty")
    else:
        print("Todo list:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}. {item}")

# Main loop
while True:
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. Display items in list")
    print("4. Quit")

    choice = input("Enter the number (1-4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)

    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)

    elif choice == '3':
        display()

    elif choice == '4':
        print("thanks for using todo list.")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 4.")