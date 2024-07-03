string = "hello world"
dups = []
count = 0
for ch in string:
    if string.count(ch) > 1 and ch not in dups:
        count += 1
        dups.append(ch)
print('The duplicate characters are {}'.format(dups))

chars = "abcdefghijklmnopqrstuvwxyz"
check_string = "hello world"

for char in chars:
    count = check_string.count(char)
    if count > 1:
        print(char, count)


