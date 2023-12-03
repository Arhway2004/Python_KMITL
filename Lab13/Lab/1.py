# def list_member(num):
#     out_put = False
#     list = [1,2,3]
#     if num == 1:  
#        return num  
#     else:  
#         if num in list:
#             out_put = True
#             return out_put

# list_member(2)
# print(list_member)

# def is_member(element, input_list):
#     if not input_list:
#         return False  # Base case: the list is empty, and the element is not found.
#     if element == input_list[0]:
#         return True  # Base case: the element is found at the beginning of the list.
#     return is_member(element, input_list[1:])  # Recursive case: check the rest of the list.

# # Example usage:
# element_to_check = 2
# my_list = [1, 2, 31]
# result = is_member(element_to_check, my_list)

# if result:
#     print(f"{element_to_check} is a member of the list.")
# else:
#     print(f"{element_to_check} is not a member of the list.")


def list_member(my_list,num):
    # my_list = [1, 2, 3]
    if num in my_list:
        return True
    else:
        return False
    
my_list = [1, 2, 31]
result = list_member(my_list, 2)

print(result)
