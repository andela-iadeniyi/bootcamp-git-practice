#Lodash for python
def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	pass

def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	pass

def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	c = []
	for key in a:
		for key2 in b:
			if key == key2:
				c.append(key)
	return c

def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''
	a = 0
	for key in haystack:
		if needle == key:
			a += 1
	return a


def sort(l):
	'''
	This function returns a sorted version of l
	'''
	pass
