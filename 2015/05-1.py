
f = open('05-input.py')

def has_three_vowels(str):
	count = 0
	for letter in str:
		if letter in ["a","e","i","o","u"]:
			count += 1
	return count > 2
	
def has_double_letter(str):
	prev = ''
	for letter in str:
		if letter == prev:
			return True
		else:
			prev = letter
	return False
	
def doesnt_have_banned_pair(str):
	for i in xrange(1,len(str)):
		pair = str[i-1] + str[i]
		if pair in ["ab","cd","pq","xy"]:
			return False
	return True

# How to call all 3 functions in a nice way?
def is_nice(str):
	if has_three_vowels(str) and has_double_letter(str) and doesnt_have_banned_pair(str):
		return True
	return False

def main():
	count = 0
	for str in f:
		if is_nice(str):
			count += 1
	print count

main()