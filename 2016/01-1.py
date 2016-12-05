
f = open('01-input.txt').read()

def main():
	x = 0
	y = 0
	d = 0 # direction: N: 0 (mod 4), E: 1 (mod 4), S: 2 (mod 4), W: 3 (mod 4)
	for instruction in f.split(','):
		instruction = instruction.strip()
		# Change direction
		d = d + (1 if instruction[0] == 'R' else -1)
		# Change position
		len = int(instruction[1:])
		if d % 4 == 0:
			y = y + len
		elif d % 4 == 1:
			x = x + len
		elif d % 4 == 2:
			y = y - len
		else:
			x = x - len
		
	print abs(x) + abs(y)

main()
