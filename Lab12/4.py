def is_subset(sub, sup):
    # Iterate through the elements in sub
    for element in sub:
        # If any element in sub is not in sup, return False
        if element not in sup:
            return False
    # If all elements in sub are found in sup, return True
    return True

superset = {1, 2, 3, 4}
subset1 = {1, 2, 4}
subset2 = {1, 2, 5}

print(is_subset(subset1, superset))
print(is_subset(subset2, superset))
