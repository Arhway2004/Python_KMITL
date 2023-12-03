# def merge(list1,list2):
#     new_list=[]
#     long = len(list1) if len(list1) > len(list2) else len(list2)
#     short = len(list1) if len(list1) < len(list2) else len(list2)
#     for x in range(long):
#         if list1[x] > list2[x]:
#             new_list.append(list2[x])
#             new_list.append(list1[x])
#         elif list1[x] < list2[x]:
#             new_list.append(list1[x]) 
#             new_list.append(list2[x])
#         else:
#             new_list.append(list1[x]) 
#             new_list.append(list2[x])
#     return new_list

# list1_input = input("Enter list1 (comma-separated integers): ")
# list1 = [int(item) for item in list1_input.split()]
# list2_input = input("Enter list2 (comma-separated integers): ")
# list2 = [int(item) for item in list2_input.split()]
# merge(list1,list2)


def merge(list1, list2):
    new_list = []
    long = len(list1) if len(list1) > len(list2) else len(list2)
    short = len(list1) if len(list1) < len(list2) else len(list2)
    for x in range(long):
        if x < short:
            if list1[x] > list2[x]:
                new_list.append(list2[x])
                new_list.append(list1[x])
            elif list1[x] < list2[x]:
                new_list.append(list1[x])
                new_list.append(list2[x])
            else:
                new_list.append(list1[x])
                new_list.append(list2[x])
        else:
            new_list.append(list1[x]) if len(list1) > len(list2) else new_list.append(list2[x])

    return new_list

list1_input = input("Enter list1 (comma-separated integers): ")
list1 = [int(item) for item in list1_input.split()]
list2_input = input("Enter list2 (comma-separated integers): ")
list2 = [int(item) for item in list2_input.split()]

merged_list = merge(list1, list2)
print("Merged List:", merged_list)
