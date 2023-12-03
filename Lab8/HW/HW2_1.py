user_input = input("Enter some text: ")
char_count = {}#dicenary
total_chars = len(user_input)

print("Character Frequency Table")

for char in user_input:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():#char:T count:6
    percentage = (count / total_chars) * 100
    print(f"{char}: {percentage:.2f}%")
