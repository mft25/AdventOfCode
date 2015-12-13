
f = open('2-input.py')

def gift_from_str(gift_str):
	gift = [int(len) for len in gift_str.split("x")]
	gift.sort()
	return gift

def main():
	area = 0
	for gift_str in f:
		gift = gift_from_str(gift_str)
		area += 3*gift[0]*gift[1]
		area += 2*gift[1]*gift[2]
		area += 2*gift[2]*gift[0]
	print area

main()