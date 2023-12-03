import pickle
import tkinter as tk
from tkinter import simpledialog

phone_book = {}

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if name:
        try:
            number = simpledialog.askstring("Add Contact", f"Enter number for {name}:")
            if number:
                phone_book[name] = number
                print(f"{name} added to the phone book.")
        except Exception as "Hello":
                print(f"Invalid")

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
