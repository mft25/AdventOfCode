
f = open('18-input.py')

def permute(array):
	new_array = [[0 for j in xrange(0,100)] for i in xrange(0,100)]
	for i in xrange(0,100):
		for j in xrange(0,100):
			neighbours = [rows[max(j-1,0):j+2] for rows in array[max(i-1,0):i+2]]
			count = sum(map(sum, neighbours)) - array[i][j]
			if count==3 or (count==2 and array[i][j]==1):
				new_array[i][j] = 1
	return new_array

def main():
	array = [[1 if light=="#" else 0 for light in line.strip()] for line in f]
	for i in xrange(0,100):
		array = permute(array)
	print sum(map(sum, array))

main()