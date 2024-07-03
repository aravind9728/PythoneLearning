def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements
        start += 1
        end -= 1
    return arr

# Example usage:
array = [1, 2, 3, 4, 5]
reversed_array = reverse_array(array)
print("Reversed Array:", reversed_array)

print(len(array))


def reverse_each_word(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse each word and store in a new list
    reversed_words = [word[::-1] for word in words]
    # Join the reversed words back into a single string
    result = ' '.join(reversed_words)
    return result

# Example usage
input_string = "hello world"
output_string = reverse_each_word(input_string)
print(output_string)  # Output: "olleh dlrow"
