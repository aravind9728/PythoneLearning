def find_missing_numbers(sequence):
    if not sequence:
        return []

    # Determine the expected range of numbers
    start, end = sequence[0], sequence[-1]
    full_set = set(range(start, end + 1))

    # Convert the sequence to a set
    sequence_set = set(sequence)

    # Find the missing numbers
    missing_numbers = sorted(full_set - sequence_set)

    return missing_numbers


# Example usage
sequence = [1, 2, 4, 6, 7, 8, 10]
missing_numbers = find_missing_numbers(sequence)
print(missing_numbers)  # Output: [3, 5, 9]
