array = [64, 25, 12, 22, 11]

count = 0
for i in array:
    count = count+1
print(count)

# initializing string
test_str = "Gfg, is best : for ! Geeks ;"

# printing original string
print("The original string is : " + test_str)

# initializing punctuations string
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
res = " "

for ele in test_str:
    if ele not in punc:
        res += ele

# printing result
print("The string after punctuation filter : " + res)


