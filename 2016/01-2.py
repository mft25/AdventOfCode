
f = open('01-input.txt').read()

def main():
	x = 0
	y = 0
	d = 0 # direction: N: 0 (mod 4), E: 1 (mod 4), S: 2 (mod 4), W: 3 (mod 4)
	visited = []
	for instruction in f.split(','):
		instruction = instruction.strip()
		# Change direction
		d = d + (1 if instruction[0] == 'R' else -1)
		# Change position
		len = int(instruction[1:])
		for i in xrange(0, len):
			print (x, y)
			visited.append((x, y))
			if d % 4 == 0:
				y = y + 1
			elif d % 4 == 1:
				x = x + 1
			elif d % 4 == 2:
				y = y - 1
			else:
				x = x - 1
			if (x, y) in visited:
				break
		
	print abs(x) + abs(y)

main()
