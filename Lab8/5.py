# def LCS(s1,s2):

# long_string = "Thisisalongstringthatcontainsashortstring."
# short_string = "string"

# index = long_string.find(short_string)

# while index != -1:
#     start = max(0, index - 10)  # Adjust the start position for context
#     end = min(len(long_string), index + len(short_string) + 10)  # Adjust the end position for context

#     overlapping_text = long_string[start:end]
#     print("Overlapping text:", overlapping_text)
    
#     index = long_string.find(short_string, index + 1)

# A="ingenious"
# B="intelligent"
# result=[]
# for x in A:
#     for y in B:
#         if x==y:
#             result+=y
# if result<2:
#     print()
# else:          
#     print(result)
# A = "ingenious"
# B = "intelligent"
# result = []

# for x in A:
#     for y in B:
#         if x == y:
#             result.append(y)
#             break
# for x in result:
#     for y in result:

# if len(result) < 2:
#     print()
# else:
#     print("".join(result))
# A = "ingenious"
# B = "intelligent"
# A = "philosophically "
# B = " zoophilous"
# result = []

# # Find common substrings and their lengths
# for i in range(len(A)):
#     for j in range(len(B)):
#         k = 0
#         while i + k < len(A) and j + k < len(B) and A[i + k] == B[j + k]:
#             k += 1
#         if k > 0:
#             result.append((A[i:i + k], k))

# # Find the common substring with the maximum overlap
# if len(result) == 0:
#     print()
# else:
#     max_overlap = max(result, key=lambda x: x[1])
#     print(max_overlap[0])

def LCS(s1,s2):
    result = []
    for i in range(len(s1)):#5
        for j in range(len(s2)):#6
            k = 0
            while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
                k += 1
                if k > 0:
                    result.append((s1[i:i + k], k))
    if len(result) == 0:
        return ""
    else:
        max_overlap = max(result, key=lambda x: x[1])
        return max_overlap[0]
    
result = LCS("intelligent","inconsidered")
print(result)