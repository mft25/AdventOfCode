
f = open('8-input.py')

def escaped_len(str):
	diff = 2
	i = 1
	while i < len(str):
		if str[i] == "\\":
			if str[i+1] == "x":
				diff += 3
				i += 3
			else:
				diff += 1
				i += 1
		i+=1
	return diff

def main():
	diff = 0
	for line in f:
		diff += escaped_len(line)
	print diff

main()