
# def find_duplicates(dict):
#     # myDict = {'s5301':'Fred','s5302':'Harry','s5303':'John','s5302':'Fred','s5305':'Harry'}
#     duplicates_dict = {}
#     for k,v in dict.items():
#         if v in dict:
#             duplicates_dict.push(k,v)
#         else:
#             pass
#     for k,v in  duplicates_dict.items():
#         print(f"{k}: {v}")

# myDict = {'s5301':'Fred','s5302':'Harry','s5303':'John','s5302':'Fred','s5305':'Harry'}
# result = find_duplicates(myDict)
def find_duplicates(input_dict):
    duplicates = {}
    seen_values = {}

    for key, value in input_dict.items():
        if value in seen_values:
            if value not in duplicates:
                duplicates[value] = [seen_values[value]]
            duplicates[value].append(key)
        else:
            seen_values[value] = key

    result_dict = {}
    for value, keys in duplicates.items():
        for key in keys:
            result_dict[key] = value

    return result_dict

# Example usage:
myDict = {'s5301': 'Fred', 's5302': 'Harry', 's5303': 'John', 's5304': 'Fred', 's5305': 'Harry'}
result = find_duplicates(myDict)
print(result)
