# # Q1
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


# # Q2
# def find_duplicates(input_dict):
#     duplicates = {}
#     seen_values = {}

#     for key, value in input_dict.items():
#         if value in seen_values:
#             if value not in duplicates:
#                 duplicates[value] = [seen_values[value]]
#             duplicates[value].append(key)
#         else:
#             seen_values[value] = key

#     result_dict = {}
#     for value, keys in duplicates.items():
#         for key in keys:
#             result_dict[key] = value

#     return result_dict

# # Example usage:
# myDict = {'s5301': 'Fred', 's5302': 'Harry', 's5303': 'John', 's5304': 'Fred', 's5305': 'Harry'}
# result = find_duplicates(myDict)
# print(result)



# Q3
# def inverse(input_dict):
#     inverse_dict = {}

#     for key, value in input_dict.items():
#         if value not in inverse_dict:
#             inverse_dict[value] = set()
#         inverse_dict[value].add(key)

#     return inverse_dict

# # Q1
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


# # Q2
# def find_duplicates(input_dict):
#     duplicates = {}
#     seen_values = {}

#     for key, value in input_dict.items():
#         if value in seen_values:
#             if value not in duplicates:
#                 duplicates[value] = [seen_values[value]]
#             duplicates[value].append(key)
#         else:
#             seen_values[value] = key

#     result_dict = {}
#     for value, keys in duplicates.items():
#         for key in keys:
#             result_dict[key] = value

#     return result_dict

# # Example usage:
# myDict = {'s5301': 'Fred', 's5302': 'Harry', 's5303': 'John', 's5304': 'Fred', 's5305': 'Harry'}
# result = find_duplicates(myDict)
# print(result)



# Q3
# def inverse(input_dict):
#     inverse_dict = {}

#     for key, value in input_dict.items():
#         if value not in inverse_dict:
#             inverse_dict[value] = set()
#         inverse_dict[value].add(key)

#     return inverse_dict

# # Example usage:
# my_dict = {'a': '1', 'b': '2', 'e': '1', 'd': '3', 'f': '1', 'g': '2'}
# result = inverse(my_dict)
# print(result)


# # Q4
# def is_subset(sub, sup):
#     # Iterate through the elements in sub
#     for element in sub:
#         # If any element in sub is not in sup, return False
#         if element not in sup:
#             return False
#     # If all elements in sub are found in sup, return True
#     return True

# # Example usage:
# superset = {1, 2, 3, 4}
# subset1 = {1, 2, 4}
# subset2 = {1, 2, 5}

# print(is_subset(subset1, superset))  # True
# print(is_subset(subset2, superset))  # False

# # Q5
# s = set([1, 2, 3])
# def powerset(s):
#     lst = list(s)
#     n = len(lst)
#     powerset = []

#     for i in range(1 << n):
#         subset = []
#         for j in range(n):
#             if (i >> j) & 1:
#                 subset.append(lst[j])
#         powerset.append(frozenset(subset))

#     return powerset

# print(powerset(s), end = "")
