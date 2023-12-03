first=input("Enter your first name:")
last=input("Enter your last name:")
gender=input("Enter your gender(m/f):")

covert = f"{gender}{last[0]}{first[0:6]}"
username=covert.upper()
print(username)