# I edited the original input file by piping through sed
f = open('6-input.py')

def read_instruction(instruction):
	parts = instruction.strip().split("|")
	parts = [int(part) for part in parts]
	return (parts[0], parts[1:3], parts[3:5])
	
def transform_grid(type, start, end, grid):
	for i in xrange(start[0], end[0]+1):
		for j in xrange(start[1], end[1]+1):
			if type == 1:
				grid[i][j] = 1 - grid[i][j]
			elif type == 2:
				grid[i][j] = 1
			elif type == 3:
				grid[i][j] = 0
	return grid

def main():
	grid = [[0 for j in xrange(0,1000)] for i in xrange(0,1000)]
	for instruction in f:
		(type, start, end) = read_instruction(instruction)
		grid = transform_grid(type, start, end, grid)
	print sum(map(sum, grid))
		
main()