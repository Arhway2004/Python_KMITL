#Question 4,5,6
while True:
    try:
        command = input("Enter file name: ")
        with open(command, "r") as file:
            content = file.read()

        old = input("Enter the old string to be replaced: ")
        new = input("Enter the new string to replace the old string: ")

        if old == new:
            raise SyntaxError

        if old in content:
            content = content.replace(old, new)
        else:
            print("The input string does not exist in the file")
            continue

        with open(command, "w") as file:
            file.write(content)

        print("Done")
        break
    except FileNotFoundError:
        print("File does not exist")
    except SyntaxError:
        print("The old string is the same as the new")