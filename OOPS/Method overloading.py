#TODO Method Overloading:
#TODO Two or more methods have the same name but different numbers of parameters or different types of parameters, or both.
#TODO These methods are called overloaded methods and this is called method overloading.


def product(a, b):
	p = a * c
	print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c): 
	p = a * b * c
	print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 3)
