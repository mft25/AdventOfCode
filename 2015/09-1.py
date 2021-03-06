from itertools import permutations

f = open('09-input.py')

def read_distance(str):
	parts = str.strip().split()
	return (parts[0], parts[2], int(parts[4]))
	
def input_to_array(array):
	places = []
	for line in f:
		(start, end, distance) = read_distance(line)
		if start not in places:
			places.append(start)
		if end not in places:
			places.append(end)
		array[places.index(start)][places.index(end)] = distance
		array[places.index(end)][places.index(start)] = distance

def main():
	array = [[0 for j in xrange(0,8)] for i in xrange(0,8)]
	input_to_array(array)
	min_distance = sum(map(sum, array))
	for permutation in permutations(range(0,8)):
		# Don't process reverse routes already processed.
		if permutation[0] > permutation[7]:
			continue
		distance = 0
		for i in xrange(1,8):
			distance += array[permutation[i]][permutation[i-1]]
			if distance > min_distance:
				continue
		min_distance = min(distance, min_distance)
	print min_distance
		
main()