# # import pickle
# # import os

# # phone_book={}

# # def add_contact():
# #     name = input("Enter name")
# #     number = input("Enter number")
# #     phone_book[name] = number
# #     print(f"{name} added to the phone book.")

# # def delete_contact():
# #     name = input("Enter name")
# #     if name in phone_book:
# #         del phone_book[name]
# #         print(f"{name} deleted from the phone book.")
# #     else:
# #         print(f"{name} not found in the phone book.")

# # def find_contact():
# #     name = input("Enter name")
# #     if name in phone_book:
# #         print(f"Phone number for {name}: {phone_book[name]}")
# #     else:
# #         print(f"{name} not found in the phone book.")

# # # def save_contacts():

# # #     filename= input("Enter name")
# # #     with open(filename,'wb') as file:
# # #         pickle.dump(phone_book,file)
# # #     print("Contacts saved to the file.")

# # def save_contacts():
# #     filename= input("Enter name")
# #     with open(filename,'wb') as file:
# #         pickle.dump(phone_book,file)
# #     try:
# #         filename in (phone_book, file)
# #     except ValueError:
# #         print("Oops!  That was no valid number.  Try again...")
        
# # def load_contacts():
# #     filename = input("Enter the file name to load contacts from: ")
# #     try:
# #         with open(filename, 'rb') as file:
# #             global phone_book
# #             phone_book = pickle.load(file)
# #         print("Contacts loaded from the file.")
# #     except FileNotFoundError:
# #         print("File not found.")
# #     except Exception as e:
# #         print(f"An error occurred: {e}")

# # def print_contacts():
# #     print("Phonebook:")
# #     for name, number in phonebook.items():
# #         print(f"{name}: {number}")

# # while True:
# #     print("\nPhonebook Manager")
# #     print("Press '+' to add a new contact.")
# #     print("Press '-' to delete a contact.")
# #     print("Press 'f' to find a contact.")
# #     print("Press 's' to save all contacts to a file.")
# #     print("Press 'l' to load previous saved contacts from a file.")
# #     print("Press 'p' to print out all contacts in the phonebook.")
# #     print("Press 'q' to quit the program.")
# #     choice = input("Enter your choice: ")
    
# #     if choice == '+':
# #         add_contact()
# #     elif choice == '-':
# #         delete_contact()
# #     elif choice == 'f':
# #         find_contact()
# #     elif choice == 's':
# #         save_contacts()
# #     elif choice == 'l':
# #         load_contacts()
# #     elif choice == 'p':
# #         print_contacts()
# #     elif choice == 'q':
# #         break
# #     else:
# #         print("Invalid choice. Please try again.")

# # print("Goodbye!")
# import pickle
# import os

# phone_book = {}

# def add_contact():
#     name = input("Enter name: ")
#     number = input("Enter number: ")
#     phone_book[name] = number
#     print(f"{name} added to the phone book.")

# def delete_contact():
#     name = input("Enter name: ")
#     if name in phone_book:
#         del phone_book[name]
#         print(f"{name} deleted from the phone book.")
#     else:
#         print(f"{name} not found in the phone book.")

# def find_contact():
#     name = input("Enter name: ")
#     if name in phone_book:
#         print(f"Phone number for {name}: {phone_book[name]}")
#     else:
#         print(f"{name} not found in the phone book.")

# def save_contacts():
#     filename = input("Enter file name to save contacts: ")
#     try:
#         with open(filename, 'wb') as file:
#             pickle.dump(phone_book, file)
#         print("Contacts saved to the file.")
#     except Exception as e:
#         print(f"An error occurred while saving contacts: {e}")

# def load_contacts():
#     filename = input("Enter the file name to load contacts from: ")
#     try:
#         with open(filename, 'rb') as file:
#             global phone_book
#             phone_book = pickle.load(file)
#         print("Contacts loaded from the file.")
#     except FileNotFoundError:
#         print("File not found.")
#     except Exception as e:
#         print(f"An error occurred while loading contacts: {e}")

# def print_contacts():
#     print("Phonebook:")
#     for name, number in phone_book.items():
#         print(f"{name}: {number}")

# while True:
#     print("\nPhonebook Manager")
#     print("Press '+' to add a new contact.")
#     print("Press '-' to delete a contact.")
#     print("Press 'f' to find a contact.")
#     print("Press 's' to save all contacts to a file.")
#     print("Press 'l' to load previously saved contacts from a file.")
#     print("Press 'p' to print out all contacts in the phonebook.")
#     print("Press 'q' to quit the program.")
#     choice = input("Enter your choice: ")
    
#     if choice == '+':
#         add_contact()
#     elif choice == '-':
#         delete_contact()
#     elif choice == 'f':
#         find_contact()
#     elif choice == 's':
#         save_contacts()
#     elif choice == 'l':
#         load_contacts()
#     elif choice == 'p':
#         print_contacts()
#     elif choice == 'q':
#         break
#     else:
#         print("Invalid choice. Please try again.")

# print("Goodbye!")


import pickle
import tkinter as tk
from tkinter import simpledialog

phone_book = {}

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if name:
        number = simpledialog.askstring("Add Contact", f"Enter number for {name}:")
        if number:
            phone_book[name] = number
            print(f"{name} added to the phone book.")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter name:")
    if name in phone_book:
        del phone_book[name]
        print(f"{name} deleted from the phone book.")
    else:
        print(f"{name} not found in the phone book.")

def find_contact():
    name = simpledialog.askstring("Find Contact", "Enter name:")
    if name in phone_book:
        print(f"Phone number for {name}: {phone_book[name]}")
    else:
        print(f"{name} not found in the phone book.")

def save_contacts():
    filename = simpledialog.askstring("Save Contacts", "Enter file name to save contacts:")
    if filename:
        try:
            with open(filename, 'wb') as file:
                pickle.dump(phone_book, file)
            print("Contacts saved to the file.")
        except Exception as e:
            print(f"An error occurred while saving contacts: {e}")

def load_contacts():
    filename = simpledialog.askstring("Load Contacts", "Enter the file name to load contacts from:")
    if filename:
        try:
            with open(filename, 'rb') as file:
                global phone_book
                phone_book = pickle.load(file)
            print("Contacts loaded from the file.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred while loading contacts: {e}")

def print_contacts():
    contact_list = "Phonebook:\n"
    for name, number in phone_book.items():
        contact_list += f"{name}: {number}\n"
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, contact_list)
    text_display.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Phonebook Manager")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

add_button = tk.Button(frame, text="Add Contact", command=add_contact)
add_button.pack(side=tk.LEFT)

delete_button = tk.Button(frame, text="Delete Contact", command=delete_contact)
delete_button.pack(side=tk.LEFT)

find_button = tk.Button(frame, text="Find Contact", command=find_contact)
find_button.pack(side=tk.LEFT)

save_button = tk.Button(frame, text="Save Contacts", command=save_contacts)
save_button.pack(side=tk.LEFT)

load_button = tk.Button(frame, text="Load Contacts", command=load_contacts)
load_button.pack(side=tk.LEFT)

print_button = tk.Button(frame, text="Print Contacts", command=print_contacts)
print_button.pack(side=tk.LEFT)

text_display = tk.Text(root, state=tk.DISABLED)
text_display.pack(padx=10, pady=10)

root.mainloop()
