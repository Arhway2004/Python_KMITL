# def get_the_difference(list1,list2):
#     result_list =[list1,list2]
#     return(result_list)


# list1 =[3,1,1,1,2,7]
# list2 =[4,1,1,2,2,5]
# get_the_difference(list1,list2)
def get_the_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    difference = list(set1.symmetric_difference(set2))
    return difference

list1 = [3, 1, 1, 1, 2, 7]
list2 = [4, 1, 1, 2, 2, 5]
result = get_the_difference(list1, list2)
print(result)
