import re

file = open('09-input.txt')

def f(input):
	regex = re.compile("([^(]*)\(([0-9]+)x([0-9]+)\)(.*)")
	match = regex.match(input)
	if match is not None:
		(pre, num_chars, num_repetitions, post) = match.groups()
		num_chars = int(num_chars)
		return len(pre) + num_chars*int(num_repetitions) + f(post[num_chars:])
	else:
		return len(input)

def main():
	input = file.read()
	print f(input)

main()	
