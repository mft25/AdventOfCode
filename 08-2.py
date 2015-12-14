
f = open('08-input.py')

def escaped_len(str):
	diff = 2
	i = 0
	while i < len(str):
		if str[i] == "\\" or str[i] == "\"":
			diff += 1
		i+=1
	return diff

def main():
	diff = 0
	for line in f:
		diff += escaped_len(line)
	print diff

main()