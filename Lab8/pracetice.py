# in1 = input("1")
# in2 = input("2")

# short = in1 if in1 < in2 else in2
# long = in1 if in1 > in2 else in2
# out = False

# for i in range(len(long)-len(short)-1):
#     if long[i:i+len(short)]==short:
#         out = True
# print(out)

def LCR(s1,s2):
    result = []
    word= ""
    short = s1 if len(s1)>len(s2) else s2
    long = s1 if len(s1)<len(s2) else s2
    for i in range(len(s1)):
        for j in range(len(s2)):
            if short[i:j+1] in long:
                result.append(short[i:j+1])

    max_len = 0
    for i in result:
        if len(i) > max_len:
            max_len = len(i)
            word = i
    return word
print(LCR("sdafsg","sdsfd"))