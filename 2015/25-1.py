
def get_index(row, col):
	t_index = row + col - 1
	t_number = (t_index*(t_index+1)) / 2
	return t_number - (row - 1)

def get_code(n):
	code = 20151125
	for i in xrange(1, n):
		code = (code*252533) % 33554393
	return code
	
def main(row, col):
	n = get_index(row, col)
	print get_code(n)

main(3010, 3019)
