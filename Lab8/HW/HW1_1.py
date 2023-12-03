user_input = int(input("Enter an integer: "))

if user_input < 0:
    print("Negative integers are not supported.")
elif user_input == 0:
    print("Binary representation: 0")
else:
    binary_string = ""
    
    while user_input > 0:
        remainder = user_input % 2
        binary_string = str(remainder) + binary_string
        user_input = user_input // 2
    
    print(f"Binary representation: {binary_string}")

    binary_str = binary_string[::-1]
    decimal_value = 0

    for i in range(len(binary_str)):
        if binary_str[i] == '1':
            decimal_value += 2 ** i

    print(f"Converted back to integer: {decimal_value}")
