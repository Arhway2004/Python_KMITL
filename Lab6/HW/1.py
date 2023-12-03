# h,m  = int(input())
def time(h=0, m=0):
    if h >= 12:
        period = "PM"
        # if h > 12:
        h -= 12
    else:
        period = "AM"
        if h == 0:
            h = 12

    return f"{h:02d}:{m:02d} {period}"

# h,m = map(int,input().split())
result = time(h=13, m=4)
print(result)

# def time(h=0, m=0):
#     if h >= 12:
#         period = "PM"
#         if h > 12:
#             h -= 12
#     else:
#         period = "AM"
#         if h == 0:
#             h = 12

#     return f"{h}:{m:02d} {period}"

# # Get user input for hours and minutes
# user_hours = int(input("Enter hours (0-23): "))
# user_minutes = int(input("Enter minutes (0-59): "))

# # Call the time function with user input
# formatted_time = time(h=user_hours, m=user_minutes)
# print("Formatted time:", formatted_time)