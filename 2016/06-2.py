
f = open('06-input.txt')

def main():
	letters = []
	for word in f:
		word = word.strip()
		if len(letters) == 0:
			letters = [{} for letter in word]
		for (i, letter) in enumerate(word):
			if letter not in letters[i]:
				letters[i][letter] = 1
			else:
				letters[i][letter] += 1
	text = ""
	for dict in letters:
		list = sorted(dict.items(), key=lambda item: item[1])
		text += list[0][0]
	print text	

main()
