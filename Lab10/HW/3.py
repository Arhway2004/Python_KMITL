def my_union(list1, list2):
    New={}

    for x in list1:
            New[x] = 1
    for x in list2:
            New[x] = 1

    return list(New)

def my_intersection(list1, list2):
    return list(set(list1).intersection(list2))

def my_difference(list1, list2):
    return list(set(list1).difference(list2))

# Example usage
list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

union_result = my_union(list1, list2)
intersection_result = my_intersection(list1, list2)
difference_result = my_difference(list1, list2)

# Format the output as specified
print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")
print(f"Difference: {difference_result}")
