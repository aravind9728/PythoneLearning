def find_min_and_max(arr):
    if not arr:
        return None  # Handle the empty array case

    min_element = arr[0]
    max_element = arr[0]

    for num in arr:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num

    return min_element, max_element


# Example usage:
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
minimum, maximum = find_min_and_max(array)
print(f"Minimum: {minimum}, Maximum: {maximum}")



def missin_int():
    if not testlist:
        return []
    start,end = testlist[0], testlist[-1]


testlist = []