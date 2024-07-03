def count_occurrences(arr, value):
    count = 0
    for elem in arr:
        if elem == value:
            count += 1
    return count

# Example usage:
array = [1, 2, 3, 4, 2, 2, 5, 2, 6]
value = 2
occurrences = count_occurrences(array, value)
print(f"The number {value} occurs {occurrences} times in the array.")



def count_occurrence(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# Example usage:
input_string = "hello world"
character_to_count = 'o'

result = count_occurrence(input_string, character_to_count)
print(f"The character '{character_to_count}' appears {result} times in the string '{input_string}'.")

def count_digit_3(start, end):
    count = 0
    for number in range(start, end + 1):
        print(number)
        count += str(number).count('3')
    return count

# Example usage
start = 30
end = 35
count = count_digit_3(start, end)
print(count)  # Output: 3 (as 30, 31, 32, 33, 34, 35 contain three 3's)
