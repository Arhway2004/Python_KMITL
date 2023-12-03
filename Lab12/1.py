phone_book = {}
def add_contact(name,number):
    phone_book[name]=number
    print(f"Added {name} with number {number} to the phone book.")

def remove_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Removed {name} from the phone book.")
    else:
        print(f"{name} is not in the phone book.")

def search_contact(name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} is not in the phone book.")

def display_contacts():
    print("Phone Book")
    for name,number in phone_book.items():
        print(f"{name}: {number}")

while True:
    print("\nPhone Book Menu:")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == "2":
        name = input("Enter name: ")
        remove_contact(name)
    elif choice == "3":
        name = input("Enter name: ")
        search_contact(name)
    elif choice == "4":
        display_contacts()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

# phonebook = {}  # Initialize an empty phone book dictionary

# def add_contact():
#     name = input("Enter the name: ")
#     number = input("Enter the phone number: ")
#     if name in phonebook:
#         print("Already add!!!")
#     elif number in phonebook:
#         print("Already add!!!")
#     else:
#         phonebook[name] = number
#         print(f"Added {name} to the phone book.")

# def delete_contact():
#     name = input("Enter the name to delete: ")
#     if name in phonebook:
#         del phonebook[name]
#         print(f"Deleted {name} from the phone book.")
#     else:
#         print(f"{name} not found in the phone book.")

# def find_contact():
#     name = input("Enter the name to find: ")
#     if name in phonebook:
#         print(f"Phone number for {name}: {phonebook[name]}")
#     else:
#         print(f"{name} not found in the phone book.")

# def print_contacts():
#     if not phonebook:
#         print("Phone book is empty.")
#     else:
#         print("Phone Book:")
#         for name, number in phonebook.items():
#             print(f"{name}: {number}")

# while True:
#     print("\nPhonebook Manager")
#     print("Press '+' to add a new contact")
#     print("Press '-' to delete a contact")
#     print("Press 'f' to find a contact")
#     print("Press 'p' to print all contacts")
#     print("Press 'q' to quit")

#     choice = input("Enter your choice: ")

#     if choice == '+':
#         add_contact()
#     elif choice == '-':
#         delete_contact()
#     elif choice == 'f':
#         find_contact()
#     elif choice == 'p':
#         print_contacts()
#     elif choice == 'q':
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")

