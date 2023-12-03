def composite(dict1, dict2):
    # Initialize an empty dictionary for the result
    result = {}

    # Iterate through the keys and values in dict1
    for key, value in dict1.items():
        # Check if the value from dict1 is a key in dict2
        if value in dict2:
            # Add the key from dict1 and the corresponding value from dict2 to the result
            result[key] = dict2[value]

    return result

# Example usage:
dict1 = {'a': 'p', 'b': 'r', 'c': 'g', 'd': 'p', 'e': 's'}
dict2 = {'p': '1', 'g': '2', 'r': '3', 's': '4'}

result = composite(dict1, dict2)
print(result)
