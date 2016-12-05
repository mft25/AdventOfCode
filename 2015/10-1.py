
def iterate(input):
	output = ""
	match = input[0]
	count = 1
	for i in xrange(1, len(input)):
		if input[i] == match:
			count += 1
		else:
			output += str(count) + match
			match = input[i]
			count = 1
	return output + str(count) + match
	
def main():
	input = "1113222113"
	for i in xrange(0,40):
		input = iterate(input)
	print len(input)
	
main()