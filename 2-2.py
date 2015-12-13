
f = open('2-input.py')

def gift_from_str(gift_str):
	gift = [int(len) for len in gift_str.split("x")]
	gift.sort()
	return gift

def main():
	ribbon = 0
	for gift_str in f:
		gift = gift_from_str(gift_str)
		ribbon += 2*gift[0]
		ribbon += 2*gift[1]
		ribbon += gift[0]*gift[1]*gift[2]
	print ribbon

main()