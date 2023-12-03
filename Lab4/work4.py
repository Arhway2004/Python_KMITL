X = input("Please enter a charecter:")
# if X.islower():
#     print("and its small-case letter is",X)
    
# elif X.isupper():
#     print("and its capital letter is",X)
# else:
#     print("")
if len(X)!=1:
    print("Error")
elif 0x30<=ord(X)<=0x39:
    print(X,"is a numeric charater.")
elif 0x41<=ord(X)<=0x5A:
    print(X,"is a capital letter and its small-case letter is",X.lower())
elif 0x61<=ord(X)<=0x7A:
    print(X,"is a small-case letter and its capital letter is",X.upper())
else:
    print("Special Character")