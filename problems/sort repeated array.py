def dutch_national_flag_sort(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1

    return arr


# Example usage:
array = [2, 0, 2, 1, 1, 0]
sorted_array = dutch_national_flag_sort(array)
print("Sorted Array:", sorted_array)
