def reverse(s):
    str1 = ""
    for i in s:
        str1 = i + str1
    return str1


s = "Sourceforge"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))
