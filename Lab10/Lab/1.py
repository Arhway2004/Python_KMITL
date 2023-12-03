# list = []
# stop = True
# while stop:
#     inp = input("Enter name:")
#     if inp == "":
#         stop = False
#     else:
#         list.append(inp)

# # for x in range(len(list)):
# print(list)
# def list(list1):
#     list1 = []
#     stop = True
#     while stop:def
#         inp = input("Enter name:")
#         if inp == "":
#             stop = False
#         else:
#             list1.append(inp)
# list1 = []
# list()
def collect_names():
    name_list = []
    stop = True
    while stop:
        inp = input("Enter name (press Enter to stop): ")
        if inp == "":
            stop = False
        else:
            name_list.append(inp)
    return name_list

result_list = collect_names()
print(result_list)
