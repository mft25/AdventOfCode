import re

f = open('08-input.txt')

height = 6
width = 50

def rect(screen, width, height):
	for i in xrange(0, height):
		for j in xrange(0, width):
			screen[i][j] = 1
	return screen

def rrow(screen, row_num, distance):
	for i in xrange(0, distance):
		screen[row_num] = screen[row_num][-1:] + screen[row_num][:-1]
	return screen

def transpose(array):
	return [list(i) for i in zip(*array)]
	
def rcol(screen, col_num, distance):
	screen = transpose(screen)
	screen = rrow(screen, col_num, distance)
	return transpose(screen)

def apply_instruction(screen, instruction):
	(type, val1, val2) = instruction
	if type == 1:
		return rect(screen, val1, val2)
	if type == 2:
		return rrow(screen, val1, val2)
	if type == 3:
		return rcol(screen, val1, val2)
		
def parse_instruction(instruction):
	regex = re.compile("([^0-9]*)([0-9]*)[^0-9]*([0-9]*)[^0-9]*")
	parsed = regex.match(instruction).groups()
	if "rect" in parsed[0]:
		return (1, int(parsed[1]), int(parsed[2]))
	if "rotate row" in parsed[0]:
		return (2, int(parsed[1]), int(parsed[2]))
	if "rotate column" in parsed[0]:
		return (3, int(parsed[1]), int(parsed[2]))
		
def main():
	screen = [[0 for j in xrange(0, width)] for i in xrange(0, height)]
	for instruction in f:
		screen = apply_instruction(screen, parse_instruction(instruction))
	print sum([sum(row) for row in screen])

main()
