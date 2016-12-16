import re

f = open('09-input.txt')

def main():
	input = f.read()
	length = 0
	regex = re.compile("([^(]*)\(([0-9]+)x([0-9]+)\)(.*)")
	while len(input) > 0:
		match = regex.match(input)
		if match is not None:
			(pre, num_chars, num_repetitions, post) = match.groups()
			length += len(pre) + int(num_chars)*int(num_repetitions)
			input = post[int(num_chars):]
		else:
			length += len(input)
			input = ""
	print length

main()	
