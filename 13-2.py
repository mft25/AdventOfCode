from itertools import permutations

f = open('13-input.py')

num_people = 9

def read_happiness(str):
	parts = str.strip().strip(".").split()
	direction = -1 if parts[2] == "lose" else 1
	return (parts[0], parts[-1], int(parts[3])*direction)

def input_to_array(array):
	people = []
	for line in f:
		(p1, p2, happiness) = read_happiness(line)
		if p1 not in people:
			people.append(p1)
		if p2 not in people:
			people.append(p2)
		array[people.index(p1)][people.index(p2)] = happiness

def main():
	array = [[0 for j in xrange(0,num_people)] for i in xrange(0,num_people)]
	input_to_array(array)
	max_happiness = sum(map(lambda row: sum([x for x in row if x < 0]), array))
	for permutation in permutations(range(0,num_people)):
		happiness = 0
		for i in xrange(0,num_people):
			happiness += array[permutation[i]][permutation[(i+1)%num_people]]
			happiness += array[permutation[(i+1)%num_people]][permutation[i]]
		max_happiness = max(happiness, max_happiness)
	print max_happiness

main()