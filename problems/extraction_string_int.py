import re

def extract_integers(input_string):
    # Find all sequences of digits in the input string
    integers = re.findall(r'\d+', input_string)
    # Convert the sequences of digits to integers
    integers = [int(num) for num in integers]
    return integers

# Example usage
input_string = "he33llo 42"
integers = extract_integers(input_string)
print(integers)  # Output: [33, 42]



def extract_strings(input_string):
    # Use regular expression to find all alphabetic substrings
    strings = re.findall(r'[a-zA-Z]+', input_string)
    return strings

# Example usage
input_string = "he33llo 42"
strings = extract_strings(input_string)
print(strings)  # Output: ['he', 'llo']
listToStr = ''.join([str(elem) for elem in strings])

print(listToStr)