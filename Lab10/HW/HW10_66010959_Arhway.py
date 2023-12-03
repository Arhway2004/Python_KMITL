# 1
import matplotlib.pyplot as plt

def pie_chart(data):
    unique_values = set(data)
    counts = [data.count(val) for val in unique_values]
    
    
    plt.figure(figsize=(8, 8))
    plt.pie(counts, startangle=140)
    plt.title("Pie Chart")

    plt.show()

data = [3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3]
pie_chart(data)
# 2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


        if not swapped:
            break

my_list = [3, 2, 9, 7, 8]
bubble_sort(my_list)
print(my_list) 
# 3
def my_union(list1, list2):
    New = {}

    for x in list1:
        New[x] = 1

    for x in list2:
        New[x] = 1
    return list(New)

def my_intersection(list1, list2):
    return list(set(list1).intersection(list2))

def my_difference(list1, list2):
    return list(set(list1).difference(list2))

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

union_result = my_union(list1, list2)
intersection_result = my_intersection(list1, list2)
difference_result = my_difference(list1, list2)

print(f"Union: {union_result}")
print(f"Intersection: {intersection_result}")
print(f"Difference: {difference_result}")

# 4
def print_table(table):
    if not table:
        print("Table is empty.")
        return

    column_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
    header = table[0]
    for i, column in enumerate(header):
        print(f"{column:{column_widths[i]}}", end=" ")
    print()

    for row in table[1:]:
        for i, value in enumerate(row):
            print(f"{value:{column_widths[i]}}", end=" ")
        print()

table1 = [
["X", "Y"],
["10", "10"],
["10", "10"],
[200, 200]
]

table2 = [
["ID", "Name", "Surname"],
["001", "Guido", "van Rossum"],
["002", "Donald", "Knuth"],
["003", "Gordon", "Moore"]
]

print_table(table1)
print()
print_table(table2)

# 5
def isAnagram(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)

result = isAnagram("silent", "listen")
print(result)



