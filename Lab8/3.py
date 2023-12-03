# long_string = "This is a long string that contains a short string."
# short_string = "short string"

# index = long_string.find(short_string)

# if index != -1:
#     print("Short string found in the long string at index:", index)
# else:
#     print("Short string not found in the long string.")

# long_string=input("Long String:")
# short_string=input("short String:")
# z=0
# for x in short_string:
#     for y in long_string:
#         if short_string==y:
#             z=+1

# if z >= 1 :
#     print("True")
# else:
#     print("False")

inp1 = input()
inp2 = input()

short = inp1 if len(inp1) < len(inp2) else inp2
long = inp1 if len(inp1) > len(inp2) else inp2
found = False 

for i in range(len(long) - len(short)+1):
    if long[i:i+len(short)] == short:
        found = True
        break
    
print(found)