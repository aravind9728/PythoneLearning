# Initialize array
arr = [5, 2, 8, 7, 1]
temp = 0

# Sort the array in ascending order
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:   #5>2
            temp = arr[i]     #5
            arr[i] = arr[j]   #2
            arr[j] = temp     #5

# Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ")
for i in range(0, len(arr)):
    print(arr[i],end=" ")