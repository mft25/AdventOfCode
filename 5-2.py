
f = open('5-input.py')

def two_pair(str):
	for i in xrange(0,len(str)-1):
		if str.index(str[i] + str[i+1]) < i-1:
			return True
	return False
	
def sandwich(str):
	for i in xrange(1,len(str)-1):
		if str[i-1] == str[i+1]:
			return True
	return False

# How to call all 3 functions in a nice way?
def is_nice(str):
	if two_pair(str) and sandwich(str):
		return True
	return False

def main():
	count = 0
	for str in f:
		if is_nice(str):
			count += 1
	print count

main()