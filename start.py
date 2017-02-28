"""practice python

do some experiments about synax of python to use it well in the furture 
"""

def make_incrementor(n):
	"""test lambda
	
	lambda expression is usually  used for anonymous functions
	
	Arguments:
		n {integrate} -- super parameter to determinate the amount of increment
	
	Returns:
		lambda expression -- omited here
	"""
	return lambda x: x + n

increment_1 = make_incrementor(1)


increment_2 = make_incrementor(2)

# use these two functions

print(increment_1(10))

print(increment_2(10))

# put lambda into filter , map and apply

foo = [2,4,3,15,121,455]

a = filter(lambda x: x % 3 ==0,foo)
print(list(a))

