# Python3 Code implementation using dictionary

# Function to iterate through every
# digit in the given number
def print_word(N):
    digits = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight',
              '9': 'Nine', '0': 'Zero'}
    for number in N:
        print(digits[number], end=' ')


# Driver code
N = "123"
print_word(N)

# This code is contributed by Pratik Gupta (guptapratik)
