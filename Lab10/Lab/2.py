# # list1 =[3,6,6,3,7,2,0,1,5,4]
# # x = len(list1)//3
# # number = 2
# # for i in range(x):
# #     del list1[number] 
# #     print(number)
# #     number +=2

# # print(list1)
def list1(list_1):
    number =2
    for i in range(len(list_1)//3):
        del list_1[number]
        number+=2
    return list_1

original_list = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
result_list = list1(original_list)
print(result_list)

# # list1 = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
# # x = len(list1) // 3  # Integer division to get the number of elements to remove

# # # Create a new list with elements from list1, excluding every third element
# # new_list1 = [list1[i] for i in range(len(list1)) if (i + 1) % 3 != 0]

# # print(new_list1)





# def remove_every_third_element(input_list):
#     number = 2
#     for i in range(len(input_list) // 3):
#         del input_list[number]
#         number += 2
#     return input_list

# original_list = [3, 6, 6, 3, 7, 2, 0, 1, 5, 4]
# result_list = remove_every_third_element(original_list)
# print(result_list)
