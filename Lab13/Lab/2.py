def list_reverse(my_list):
    new_list = []
    if my_list == my_list:
        return my_list
    else:
        # new_list.add.my_list[-my_list]
        new_list.append(my_list[-my_list])
    return my_list


my_list = [1,2,3]
print(list_reverse(my_list))


def list_reverse(my_list):
    if not my_list:  # Base case: if the list is empty, return an empty list
        return []
    else:
        first_item = my_list[0]  # Get the first item in the list
        rest_of_list = my_list[1:]  # Get the rest of the list
        reversed_rest = list_reverse(rest_of_list)  # Recursively reverse the rest
        return reversed_rest + [first_item]  # Combine the first item with the reversed rest

my_list = [1, 2, 3]
reversed_list = list_reverse(my_list)
print(reversed_list)
