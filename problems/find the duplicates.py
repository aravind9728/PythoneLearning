def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num not in seen:
            seen.add(num)
        else:
            duplicates.add(num)
    return list(duplicates)

# Example usage:
array = [1, 2, 3, 4, 2, 3, 5, 6, 3]
duplicates = find_duplicates(array)
print("Duplicates:", duplicates)


A = set(array)
print(A)
