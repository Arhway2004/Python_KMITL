def zerosum(lst, index=0, current_subset=None, result=None):
    if current_subset is None:
        current_subset = []
    if result is None:
        result = []
    if index == len(lst):
        if sum(current_subset) == 0 and len(current_subset) != 0:
            result.append(current_subset.copy())
        return
    current_subset.append(lst[index])
    zerosum(lst, index + 1, current_subset, result)
    current_subset.pop()
    zerosum(lst, index + 1, current_subset, result)
    if index == 0:
        if len(result) <= 1:
            return "No"
        else:
            return f"Yes {result}"

lst1 = [-7, -3, -2, 5, 7,9]
lst2 = [2, -3, 5, 8, 11, 23, -1]
print(zerosum(lst1))
print(zerosum(lst2))