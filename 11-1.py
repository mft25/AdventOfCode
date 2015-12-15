
def increment(input, i):
	# Won't increment "zzzzzzzz" correctly
	j = len(input) - i - 1
	array = list(input)
	if array[j] == "z":
		array[j] = "a"
		return increment("".join(array), i+1)
	else:
		array[j] = chr(ord(array[j]) + 1)
	return "".join(array)
	
def has_pairs(str, lim):
	count = 0
	prev = ''
	for letter in str:
		if letter == prev:
			count += 1
			prev = ""
			if count >= lim:
				return True
		else:
			prev = letter
	return False
	
def has_consecutive_increments(array, lim):
	count = 1
	prev = array[0]
	for letter in array[1:]:
		if ord(letter) == ord(prev) + 1:
			count += 1
			if count >= lim:
				return True
		else:
			count = 1
		prev = letter
	return False
	
def valid_password(password):
	array = list(password)
	if "i" in array or "o" in array or "l" in array:
		return False
	if not has_pairs(password, 2):
		return False
	return has_consecutive_increments(array, 3)

def main():
	input = "hepxcrrq"
	while not valid_password(input):
		input = increment(input, 0)
	print input
		
main()