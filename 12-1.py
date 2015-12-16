import re

f = open('12-input.py')

def main():
	input = f.read()
	input = re.sub("[^-0-9]", "#", input)
	input = re.sub("#+", "#", input)
	input = input.strip("#")
	print sum([int(num) for num in input.split("#")])
	
main()