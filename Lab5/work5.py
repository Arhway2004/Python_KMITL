# while True: #x == "\t":
#     X = input("Please enter a charecter:")
#     if X == "\t":
#         print("Good bye, see you tomorrow: <tab>")
#         break
#     elif len(X) != 1:
#         print("Error")
#     elif 0x30 <= ord(X) and 0x39 >= ord(X):
#         print(X,"is a numeric charater.")
#     elif 0x41 <= ord(X) and 0x5A >= ord(X):
#         print(X,"is a capital letter and its small-case letter is",X.lower())
#     elif 0x61 <= ord(X) and 0x7A >= ord(X):
#         print(X,"is a small-case letter and its capital letter is",X.upper())
#     else:
#         print(X,"Special Character")

def character_classification(char):
    if len(char) != 1:
        return "Error"
    elif char == "\t":
        return "Goodbye, see you tomorrow: <tab>"
    elif 0x30 <= ord(char) <= 0x39:
        return f"{char} is a numeric character."
    elif 0x41 <= ord(char) <= 0x5A:
        return f"{char} is a capital letter and its small-case letter is {char.lower()}"
    elif 0x61 <= ord(char) <= 0x7A:
        return f"{char} is a small-case letter and its capital letter is {char.upper()}"
    else:
        return f"{char} Special Character"

while True:
    user_input = input("Please enter a character:")
    result = character_classification(user_input)
    print(result)
    if "\t" in result:
        break