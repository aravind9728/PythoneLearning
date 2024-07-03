list2= [3,4,2,7,8]
list1 = ["q","b","c","d"]
# for i in list2:
#     if i <= 2:
#         print(i)
# list1.append()
# list1.insert(0,"value")
# list1.extend(list2)
# list1.sort(reverse=True)
# print("a" in list1) # return true or false checking for the value
# course_str = "-".join(list1) # to string
# ne_list = course_str.split("-") # to list
#
# list1.pop()
# list1.reverse()
# list1.remove()

# print(list2[::])


mycomp = [(s,n) for s in "list2" for n in range(3) ]
# print(mycomp)

mydict = {}


for list1,list2 in zip(list1,list2):
    mydict[list1] = list2

print(mydict)
list3= ["test","bat","wayne","test2"]
mydict1 = {key:vaule for key, vaule in zip(list1,list3)}
print(mydict1)

nums = [1,2,3,4,5,6,7,8,9,10,10]


test = [n for n in nums]
test1 = {n for n in nums if n%3} # set no duplicates
print(test)
print(test1)


my_gen = [n*n for n in nums ]

print(my_gen)
for i in my_gen:
    print(i)