import re

f = open('12-input.py')

def evaluate_basic(matches):
	input = matches.group(1)
	if input[0] == "{" and "red" in input:
		return "#"
	input = re.sub("[^-0-9]", "#", input)
	input = re.sub("#+", "#", input)
	input = input.strip("#")
	if input == "":
		return "#"
	return "#" + str(sum([int(num) for num in input.split("#")])) + "#"

def evaluate(input):
	input = re.sub(r"({[^{}\[\]]*})", evaluate_basic, input)
	input = re.sub(r"(\[[^{}\[\]]*\])", evaluate_basic, input)
	return input

def main():
	input = f.read()
	old_input = ""
	while input != old_input:
		old_input = input
		input = evaluate(old_input)
	print input.strip("#")
	
main()