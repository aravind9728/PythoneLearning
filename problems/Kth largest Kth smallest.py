def kth_largest_and_smallest(arr, k):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    kth_smallest = sorted_arr[k - 1]
    kth_largest = sorted_arr[-k]
    return kth_smallest, kth_largest



# Example usage:
array = [1,5,3,9,7,13,11,17,15]
k = 3
kth_smallest, kth_largest = kth_largest_and_smallest(array, k)
print(f"{k}th Smallest: {kth_smallest}, {k}th Largest: {kth_largest}")
