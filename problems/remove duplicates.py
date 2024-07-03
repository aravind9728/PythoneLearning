def remove_duplicates(arr):
    if not arr:
        return []
    arr.sort()
    unique_array = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] not in unique_array:
        # if arr[i] != arr[i - 1]:
            unique_array.append(arr[i])
    return unique_array

# Example usage:
array = [1, 2, 3, 4, 2, 3, 5, 6, 3]
unique_array = remove_duplicates(array[:])
print("Array without duplicates:", unique_array)



def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

# Example usage
input_string = "hello world"
output_string = remove_duplicates(input_string)
print(output_string)  # Output: "helo wrd"
