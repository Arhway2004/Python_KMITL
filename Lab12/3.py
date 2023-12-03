def inverse(input_dict):
    inverse_dict = {}

    for key, value in input_dict.items():
        if value not in inverse_dict:
            inverse_dict[value] = set()
        inverse_dict[value].add(key)

    return inverse_dict

my_dict = {'a': '1', 'b': '2', 'e': '1', 'd': '3', 'f': '1', 'g': '2'}
result = inverse(my_dict)
print(result)
