def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the sorting process
        swapped = False

        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap them if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage
my_list = [3, 2, 9, 7, 8]
bubble_sort(my_list)
print(my_list)  # Output: [2, 3, 7, 9, 81]
