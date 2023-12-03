def isAnagram(string1, string2):
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    return sorted(string1) == sorted(string2)

result = isAnagram("silent", "listen")
print(result)
