# def count_digit(x):
#     total=0
#     while x > 0:
#         total+=(x%10)
#         x//=10
#     return total
# x=int(input("number:"))
# print(count_digit(x))

# def time_covert(h,m,s):
#     if h>=12:
#         period="PM"
#         if h>12:
#             h-=12
#     else:
#         period = "AM"
#         if h==24:
#             h=0
#     return f"{h}:{m}:{s}:{period}"

# h=int(input())
# m=int(input())
# s=int(input())
# print(time_covert(h,m,s))

# def reverse(x):
#     return int(str(x)[::-1])
# ip=int(input())
# print(reverse(ip))